import java.time.Duration;
import java.util.Arrays;
import java.util.Collections;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.StringDeserializer;

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
    KafkaConsumerClose.run();

  }

}

class KafkaConsumerNew {
  static KafkaConsumer<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
    configs.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

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
    // consumer.subscribe(Pattern.compile("abc*")); // pattern

    // and then must pool the records...
  }
}

class KafkaConsumerAssign {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // assign: specify a partition to read from
    TopicPartition partitionToReadFrom = new TopicPartition("my-topic", 0);
    consumer.assign(Collections.singletonList(partitionToReadFrom));
  }
}

class KafkaConsumerSeek {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // assign and seek: specify a partition and offset to read from
    TopicPartition partitionToReadFrom = new TopicPartition("my-topic", 0);
    long offsetToReadFrom = 1L;
    // consumer.seek(partitionToReadFrom, offsetToReadFrom);

  }
}

class KafkaConsumerPool {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();
    consumer.subscribe(Collections.singletonList("my-topic"));

    // poll for new data during 1 second
    // surround it with a while(true) to read forever
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(1000));

    // process the data retrieved
    if (records.isEmpty()) {
      System.out.println("no data");
      return;
    }
    for (ConsumerRecord<String, String> record : records) {
      System.out.println(record.toString());
    }

  }
}

class KafkaConsumerClose {
  static void run() {
    KafkaConsumer<String, String> consumer = KafkaConsumerNew.run();

    // close connection
    consumer.close(); // implement the interface Closeable to force its implementation
  }
}