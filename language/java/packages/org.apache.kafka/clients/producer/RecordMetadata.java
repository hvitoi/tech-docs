import java.util.Properties;
import java.util.concurrent.ExecutionException;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;

// It's the output after sending a record

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    RecordMetadataNew.run();

    /**
     * Instance
     */
    RecordMetadataTopic.run();
    RecordMetadataPartition.run();
    RecordMetadataOffset.run();
    RecordMetadataTimestamp.run();

  }
}

class RecordMetadataNew {
  static RecordMetadata run() {
    // config
    Properties configs = new Properties();
    configs.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    configs.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    // producer
    KafkaProducer<String, String> producer = new KafkaProducer<>(configs);

    // record
    ProducerRecord<String, String> record = new ProducerRecord<>("my-topic", null, "hello");

    // record metadata
    RecordMetadata recordMetadata;
    try {
      recordMetadata = producer.send(record).get();
      return recordMetadata;
    } catch (InterruptedException | ExecutionException e) {
      return null;
    }

  }
}

class RecordMetadataTopic {
  static void run() {
    RecordMetadata recordMetadata = RecordMetadataNew.run();
    String topic = recordMetadata.topic();
  }
}

class RecordMetadataPartition {
  static void run() {
    RecordMetadata recordMetadata = RecordMetadataNew.run();
    int partition = recordMetadata.partition();
  }
}

class RecordMetadataOffset {
  static void run() {
    RecordMetadata recordMetadata = RecordMetadataNew.run();
    long offset = recordMetadata.offset();
  }
}

class RecordMetadataTimestamp {
  static void run() {
    RecordMetadata recordMetadata = RecordMetadataNew.run();
    long timestamp = recordMetadata.timestamp();
  }
}
