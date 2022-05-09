import java.time.Duration;
import java.util.Arrays;
import java.util.Collections;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.StringSerializer;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    KafkaConsumerNew.run();

    /**
     * Instance
     */
    KafkaConsumerSubscribe.run();
    KafkaConsumerAssign.run();
    KafkaConsumerSeek.run();

    KafkaConsumerPool.run();

  }

}

class KafkaConsumerNew {
  static KafkaConsumer<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(configs);
    return consumer;
  }

}

class KafkaConsumerSubscribe {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // subscribe
    consumer.subscribe(Collections.singletonList("my-topic")); // single topic
    consumer.subscribe(Arrays.asList("my-topic1", "my-topic2")); // list of topics

    // and then pool the records...
  }
}

class KafkaConsumerAssign {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // assign
    TopicPartition partitionToReadFrom = new TopicPartition("my-topic", 0);

    // specify a partition to read from
    consumer.assign(Collections.singletonList(partitionToReadFrom));

  }
}

class KafkaConsumerSeek {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // assign and seek
    TopicPartition partitionToReadFrom = new TopicPartition("my-topic", 0);
    long offsetToReadFrom = 15L;

    // start from offset 15 in partition 0
    consumer.seek(partitionToReadFrom, offsetToReadFrom);

  }
}

class KafkaConsumerPool {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();
    consumer.subscribe(Collections.singletonList("my-topic"));

    // poll for new data
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

    for (ConsumerRecord<String, String> record : records) {
      System.out.println(record.toString());
    }

  }
}