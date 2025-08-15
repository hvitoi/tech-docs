import java.time.Duration;
import java.util.Collections;
import java.util.Iterator;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    ConsumerRecordsNew.run();

    /**
     * Instance
     */
    ConsumerRecordsIsEmpty.run();
    ConsumerRecordsIterator.run();

  }

}

class ConsumerRecordsNew {
  static ConsumerRecords<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
    configs.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(configs);

    consumer.subscribe(Collections.singletonList("my-topic"));

    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

    return records;
  }

}

class ConsumerRecordsIsEmpty {
  static void run() {
    ConsumerRecords<String, String> records = ConsumerRecordsNew.run();
    records.isEmpty();
  }
}

class ConsumerRecordsIterator {
  static void run() {
    ConsumerRecords<String, String> records = ConsumerRecordsNew.run();
    Iterator<ConsumerRecord<String, String>> it = records.iterator();

    if (it.hasNext()) {
      ConsumerRecord<String, String> record = it.next();
    }
  }
}
