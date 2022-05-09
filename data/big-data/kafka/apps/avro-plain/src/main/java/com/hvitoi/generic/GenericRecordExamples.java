package com.hvitoi.generic;

import java.io.IOException;
import java.io.File;

import org.apache.avro.Schema;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.generic.GenericRecordBuilder;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;

public class GenericRecordExamples {
  public static void main(String[] args) {

    // Define schema
    Schema.Parser parser = new Schema.Parser();
    Schema schema = parser.parse(
      "{\n" +
      "  \"type\": \"record\",\n" +
      "  \"namespace\": \"com.example\",\n" +
      "  \"name\": \"Customer\",\n" +
      "  \"fields\": [\n" +
      "    { \"name\": \"first_name\", \"type\": \"string\" },\n" +
      "    { \"name\": \"last_name\", \"type\": \"string\" },\n" +
      "    { \"name\": \"age\", \"type\": \"int\" },\n" +
      "    { \"name\": \"height\", \"type\": \"float\" },\n" +
      "    { \"name\": \"weight\", \"type\": \"float\" },\n" +
      "    { \"name\": \"automated_email\", \"type\": \"boolean\", \"default\": true }\n" +
      "  ]\n" +
      "}"
    );

    // Create generic record
    GenericRecordBuilder customerBuilder = new GenericRecordBuilder(schema);
    customerBuilder.set("first_name", "John"); // if no value is defined, it will fail because it has no default value
    customerBuilder.set("last_name", "Doe");
    customerBuilder.set("age", 25);
    customerBuilder.set("height", 170f);
    customerBuilder.set("weight", 80.5f);
    customerBuilder.set("automated_email", false); // if no value is defined, the default value in the schema is used
    GenericData.Record customer = customerBuilder.build();
    System.out.println(customer);

    // Write Generic Record to an AVRO file (binary format)
    final DatumWriter<GenericRecord> writer = new GenericDatumWriter<GenericRecord>(schema);
    try {
      // Open file writer
      DataFileWriter<GenericRecord> dataFileWriter = new DataFileWriter<GenericRecord>(writer);

      // Add data
      dataFileWriter.create(customer.getSchema(), new File("customer-generic.avro"));
      dataFileWriter.append(customer);
      System.out.println("File Written (customer-generic.avro)");

      // Close file writer
      dataFileWriter.close();
    } catch (IOException e) {
      System.out.println("Couldn't write file");
      e.printStackTrace();
    }

    // Read Generic Record from AVRO file (binary format)
    final File file = new File("customer-generic.avro");
    final DatumReader<GenericRecord> reader = new GenericDatumReader<GenericRecord>();
    try {
      // open file reader
      final DataFileReader<GenericRecord> dataFileReader = new DataFileReader<GenericRecord>(file, reader);
      
      while (dataFileReader.hasNext()) {
        GenericRecord customerRead = dataFileReader.next();
        System.out.println("Reading generic record");
        System.out.println(customerRead.toString()); // get whole record
        System.out.println("First name: " + customerRead.get("first_name")); // get specific field from record
        System.out.println("Non existent field: " + customerRead.get("not_here")); // get a non existent field
      }

      // close file reader
      dataFileReader.close();
    }
    catch(IOException e) {
      e.printStackTrace();
    }

    // Interpret as a generic record
  }
}
