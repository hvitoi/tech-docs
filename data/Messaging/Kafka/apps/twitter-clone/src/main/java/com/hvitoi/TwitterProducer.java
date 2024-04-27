package com.hvitoi;

import java.util.List;
import java.util.Properties;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

import com.google.common.collect.Lists;
import com.twitter.hbc.ClientBuilder;
import com.twitter.hbc.core.Client;
import com.twitter.hbc.core.Constants;
import com.twitter.hbc.core.Hosts;
import com.twitter.hbc.core.HttpHosts;
import com.twitter.hbc.core.endpoint.StatusesFilterEndpoint;
import com.twitter.hbc.core.processor.StringDelimitedProcessor;
import com.twitter.hbc.httpclient.auth.Authentication;
import com.twitter.hbc.httpclient.auth.OAuth1;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TwitterProducer {

  static Logger logger = LoggerFactory.getLogger(TwitterProducer.class.getName());

  public TwitterProducer() {}

  public static void main(String[] args) {
    new TwitterProducer();
    TwitterProducer.run();
  }

  public static void run() {
    logger.info("Setup");

    // twitter client
    List<String> terms = Lists.newArrayList("bitcoin", "football", "usa"); // terms to search
    BlockingQueue<String> msgQueue = new LinkedBlockingQueue<String>(1000); // queue with capacity of 1000 msgs
    Client twitterClient = createTwitterClient(msgQueue, terms);
    
    twitterClient.connect();  // Attempts to establish a connection

    // kafka producer client
    KafkaProducer<String, String> kafkaProducer = createKafkaProducer();

    // Shutdown hook
    // Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    //   logger.info("stopping application");
    //   twitterClient.stop();
    //   kafkaProducer.close();
    //   logger.info("done");
    // }));

    // Loop through tweets and send to kafka
    while (!twitterClient.isDone()) {
      String msg = null;
      try {
        msg = msgQueue.poll(5, TimeUnit.SECONDS);
      } catch (InterruptedException e) {
        e.printStackTrace();
        twitterClient.stop();
      }
      if (msg != null) {
        logger.info(msg);
        ProducerRecord<String, String> record = new ProducerRecord<String,String>("tweets", null, msg);
        kafkaProducer.send(record, new Callback(){
          //@Override
          public void onCompletion(RecordMetadata recordMetadata, Exception e) {
            if (e != null) {
              logger.error("Something bad happened", e);
            } 
          }
        });
      }
}
  }

  static public Client createTwitterClient(BlockingQueue<String> msgQueue, List<String> terms) {
    String apiKey = "api-key";
    String apiSecretKey = "api-secret-key";
    String accessToken = "access-token";
    String accessTokenSecret = "access-token-secret";

    // Host&Endpoint config
    Hosts hosebirdHosts = new HttpHosts(Constants.STREAM_HOST);
    StatusesFilterEndpoint hosebirdEndpoint = new StatusesFilterEndpoint();
    
    // Tweet terms to search
    hosebirdEndpoint.trackTerms(terms);

    // Oauth config
    Authentication hosebirdAuth = new OAuth1(apiKey, apiSecretKey, accessToken, accessTokenSecret);

    // Create client
    ClientBuilder builder = new ClientBuilder()
      .name("Hosebird-Client-01") // optional: mainly for the logs
      .hosts(hosebirdHosts)
      .authentication(hosebirdAuth)
      .endpoint(hosebirdEndpoint)
      .processor(new StringDelimitedProcessor(msgQueue));

    Client hosebirdClient = builder.build();
    return hosebirdClient;
   
  }

  static public KafkaProducer<String, String> createKafkaProducer() {
    String bootstrapServers = "localhost:9092";

    // producer properties
    Properties properties = new Properties();
    properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
    properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    // idempotent producer properties
    properties.setProperty(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, "true");
    properties.setProperty(ProducerConfig.ACKS_CONFIG, "all"); // not necessary (implicit in idempotence=true)
    properties.setProperty(ProducerConfig.RETRIES_CONFIG, Integer.toString(Integer.MAX_VALUE)); // not necessary (implicit in idempotence=true)
    properties.setProperty(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, "5"); // not necessary (implicit in idempotence=true)
    // batch properties
    properties.setProperty(ProducerConfig.COMPRESSION_TYPE_CONFIG, "snappy"); // none (default), gzip, lz4, snappy
    properties.setProperty(ProducerConfig.LINGER_MS_CONFIG, "20ms");
    properties.setProperty(ProducerConfig.BATCH_SIZE_CONFIG, Integer.toString(32*1024));

    // producer client
    KafkaProducer<String, String> producer = new KafkaProducer<String, String>(properties);
    return producer;
  }
}
