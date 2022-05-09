package com.hvitoi.producer;

import java.util.Properties;

import com.example.Customer;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;

import io.confluent.kafka.serializers.KafkaAvroSerializer;

public class Producer {
  public static void main(String[] args) {
    Properties properties = new Properties();
    // normal config
    properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    properties.setProperty(ProducerConfig.ACKS_CONFIG, "all");
    properties.setProperty(ProducerConfig.RETRIES_CONFIG, "10");
    // avro config
    properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());
    properties.setProperty("schema.registry.url", "localhost:9095");
    properties.setProperty("schema.registry.ssl.truststore.type", "jks");
    properties.setProperty("schema.registry.ssl.truststore.location", "./src/main/resources/certs/ca.jks");
    properties.setProperty("schema.registry.ssl.truststore.password", "...");
    // security config
    properties.setProperty("security.protocol", "ssl");
    properties.setProperty("ssl.truststore.type", "jks");
    properties.setProperty("ssl.truststore.location", "./src/main/resources/certs/cacorp.jks");
    properties.setProperty("ssl.truststore.password", "...");

    // producer client
    Producer<String, Customer> producer = new KafkaProducer<String, Customer>(properties);

    // new record
    String topic = "customer-avro";
    Customer customer = Customer.newBuilder().setFirstName("John").setLastName("Doe").setAge(34).setHeight(178f)
        .setWeight(75f).setAutomatedEmail(false).build();
    ProducerRecord<String, Customer> record = new ProducerRecord<String, Customer>(topic, customer);
    System.out.println(customer);

    // send record
    producer.send(record, new Callback() {
      @Override
      public void onCompletion(RecordMetadata metadata, Exception e) {
        if (e == null) {
          System.out.println(metadata);
        } else {
          e.printStackTrace();
        }
      }
    });

    producer.flush();
    producer.close();
  }
}
