package com.hvitoi;

import com.google.gson.JsonParser;
import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.CredentialsProvider;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.elasticsearch.action.admin.indices.create.CreateIndexRequest;
import org.elasticsearch.action.bulk.BulkRequest;
import org.elasticsearch.action.bulk.BulkResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.mapper.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

public class ElasticSearchConsumer {

  public static RestHighLevelClient createElasticSearchClient(){

    String hostname = "localhost";

    // Authentication
    // final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
    // credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials("username", "password"));

    RestClientBuilder builder = RestClient.builder(new HttpHost(hostname, 443, "https"));
      // .setHttpClientConfigCallback(new RestClientBuilder.HttpClientConfigCallback() {
      //   @Override
      //   public HttpAsyncClientBuilder customizeHttpClient(HttpAsyncClientBuilder httpClientBuilder) {
      //       return httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
      //   }
      // });

    RestHighLevelClient client = new RestHighLevelClient(builder);
    return client;
  }

  public static KafkaConsumer<String, String> createKafkaConsumerClient(String topic){

      String bootstrapServers = "localhost:9092";
      String groupId = "kafka-demo-elasticsearch";

      // consumer config
      Properties properties = new Properties();
      properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
      properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
      properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
      properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, groupId);
      properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
      properties.setProperty(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "false"); // at least once
      properties.setProperty(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, "10"); // receive a maximum of 10 records in the batch

      // consumer client
      KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(properties);
      consumer.subscribe(Arrays.asList(topic));

      return consumer;

  }

  public static void main(String[] args) throws IOException {
    Logger logger = LoggerFactory.getLogger(ElasticSearchConsumer.class.getName());

    // ElasticSearch client
    RestHighLevelClient elasticSearchClient = createElasticSearchClient();

    // Kafka Consumer client
    KafkaConsumer<String, String> kafkaConsumerClient = createKafkaConsumerClient("tweets");

    // Single request
    // IndexRequest indexRequest = new IndexRequest("tweets").source("{\"foo\":\"bar\"}", XContentType.JSON);
    // IndexResponse indexResponse = client.index(indexRequest, RequestOptions.DEFAULT);
    // String id = indexResponse.getId();

    // Bulk request
    while(true){
      // Pool kafka topic data
      ConsumerRecords<String, String> records = kafkaConsumerClient.poll(Duration.ofMillis(100));

      Integer recordCount = records.count();
      logger.info("Received " + recordCount + " records");

      // Add documents to bulk request
      BulkRequest bulkRequest = new BulkRequest();
      for (ConsumerRecord<String, String> record : records){
        try {
          // Generate ID for the document (this makes the consumer idempotent)
          //String documentId = record.topic() + "_" + record.partition() + "_" + record.offset(); // Get from kafka metadata
          String documentId = JsonParser
            .parseString(record.value())
            .getAsJsonObject()
            .get("id_str")
            .getAsString(); // Get from tweet ID

          // Add data to "tweets" index
          IndexRequest indexRequest = new IndexRequest("tweets")
            .source(record.value(), XContentType.JSON) // data to be inserted
            .id(documentId); // id of the document

          bulkRequest.add(indexRequest); // we add to our bulk request (takes no time)
        } catch (NullPointerException e){
          logger.warn("skipping bad data: " + record.value());
        }

      }

      if (recordCount > 0) {
        // Send bulk request
        BulkResponse bulkResponse = elasticSearchClient.bulk(bulkRequest, RequestOptions.DEFAULT);
        logger.info(bulkResponse.toString());

        logger.info("Committing offsets...");
        kafkaConsumerClient.commitSync();
        logger.info("Offsets have been committed");

        try {
          Thread.sleep(1000); // introduce a small delay
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
      }
    }

    // client.close();

  }
}