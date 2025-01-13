package com.hvitoi.consumer;

import com.example.Customer;
import io.confluent.kafka.serializers.KafkaAvroDeserializer;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Collections;
import java.util.Properties;

public class Consumer {

    public static void main(String[] args) {
        Properties properties = new Properties();
        // normal config
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.put(ConsumerConfig.GROUP_ID_CONFIG, "customer-consumer-group-v1");
        properties.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "false");
        properties.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        // avro config
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
        properties.setProperty("specific.avro.reader", "true");
        properties.setProperty("schema.registry.url", "localhost:9095");
        properties.setProperty("schema.registry.ssl.truststore.type", "jks");
        properties.setProperty("schema.registry.ssl.truststore.location", "./src/main/resources/certs/ca.jks");
        properties.setProperty("schema.registry.ssl.truststore.password", "...");
        // security config
        properties.setProperty("security.protocol", "ssl");
        properties.setProperty("ssl.truststore.type", "jks");
        properties.setProperty("ssl.truststore.location", "./src/main/resources/certs/ca.jks");
        properties.setProperty("ssl.truststore.password", "...");

        // consumer client
        KafkaConsumer<String, Customer> consumer = new KafkaConsumer<>(properties);

        // subscribe to topic
        String topic = "customer-avro";
        consumer.subscribe(Collections.singleton(topic));

        System.out.println("Waiting for data...");
        while (true) {
            System.out.println("Polling");
            ConsumerRecords<String, Customer> records = consumer.poll(1000);

            for (ConsumerRecord<String, Customer> record : records) {
                Customer customer = record.value();
                System.out.println(customer);
            }

            consumer.commitSync(); // commit offset
        }
    }
}
