import java.util.Properties;
import java.util.concurrent.Future;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    KafkaProducerNew.run();

    /**
     * Instance
     */
    KafkaProducerSend.run();
    KafkaProducerFlush.run();
    KafkaProducerClose.run();
  }

}

class KafkaProducerNew {
  static KafkaProducer<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    configs.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    KafkaProducer<String, String> producer = new KafkaProducer<>(configs);
    return producer;
  }

}

class KafkaProducerSend {
  static void run() {
    ProducerRecord<String, String> record = new ProducerRecord<>("my-topic", "abc", "hello");
    KafkaProducer<String, String> producer = KafkaProducerNew.run();

    // send(record)
    Future<RecordMetadata> sent1 = producer.send(record);

    // send(record, callback)
    Future<RecordMetadata> sent2 = producer.send(record, (data, e) -> {
      if (e != null) {
        e.printStackTrace();
        return;
      }
      System.out.println(data.toString());
    });

    // send(record, callback)
    Future<RecordMetadata> sent3 = producer.send(record, new Callback() {
      public void onCompletion(RecordMetadata recordMetadata, Exception e) {
        // ...
      }
    });

    producer.close();
  }
}

class KafkaProducerFlush {
  static void run() {
    KafkaProducer<String, String> producer = KafkaProducerNew.run();

    // flush only
    producer.flush();
  }
}

class KafkaProducerClose {
  static void run() {
    KafkaProducer<String, String> producer = KafkaProducerNew.run();

    // flush and close
    producer.close(); // implement the interface Closeable to force its implementation
  }
}
