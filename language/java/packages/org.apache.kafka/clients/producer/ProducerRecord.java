import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    ProducerRecordNew.run();

  }

}

class ProducerRecordNew {
  static void run() {
    // topic & value
    ProducerRecord<String, String> record1 = new ProducerRecord<>("my-topic", "hello");

    // topic & key & value
    ProducerRecord<String, String> record2 = new ProducerRecord<>("my-topic", "abc", "hello");

  }

}
