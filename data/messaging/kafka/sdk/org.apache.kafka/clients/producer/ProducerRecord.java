import org.apache.kafka.clients.producer.ProducerRecord;

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
