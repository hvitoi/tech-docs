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
    ConsumerRecordNew.run();

    /**
     * Instance
     */
    ConsumerRecordKey.run();
    ConsumerRecordValue.run();
    ConsumerRecordTopic.run();
    ConsumerRecordPartition.run();
    ConsumerRecordOffset.run();

  }

}

class ConsumerRecordNew {
  static ConsumerRecord<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    configs.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
    configs.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(configs);

    consumer.subscribe(Collections.singletonList("my-topic"));

    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

    Iterator<ConsumerRecord<String, String>> it = records.iterator();

    if (it.hasNext()) {
      ConsumerRecord<String, String> record = it.next();
      return record;
    }
    return null;
  }

}

class ConsumerRecordKey {
  static void run() {
    ConsumerRecord<String, String> record = ConsumerRecordNew.run();

    if (record != null) {
      record.key();
    }
  }
}

class ConsumerRecordValue {
  static void run() {
    ConsumerRecord<String, String> record = ConsumerRecordNew.run();

    if (record != null) {
      record.value();
    }
  }
}

class ConsumerRecordTopic {
  static void run() {
    ConsumerRecord<String, String> record = ConsumerRecordNew.run();

    if (record != null) {
      record.topic();
    }
  }
}

class ConsumerRecordPartition {
  static void run() {
    ConsumerRecord<String, String> record = ConsumerRecordNew.run();

    if (record != null) {
      record.partition();
    }
  }
}

class ConsumerRecordOffset {
  static void run() {
    ConsumerRecord<String, String> record = ConsumerRecordNew.run();

    if (record != null) {
      record.offset();
    }
  }
}
