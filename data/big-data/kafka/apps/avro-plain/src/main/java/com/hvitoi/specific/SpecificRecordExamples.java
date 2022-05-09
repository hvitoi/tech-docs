package com.hvitoi.specific;

import java.io.File;
import java.io.IOException;

import com.example.Customer;

import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.avro.specific.SpecificDatumWriter;

public class SpecificRecordExamples {
  public static void main(String[] args) {
    // Here the java class "Customer" was automatically created 
    // The schema was generated using the maven plugin using the avsc schema

    // Create specific record 
    Customer.Builder customerBuilder = Customer.newBuilder();
    customerBuilder.setAge(25);
    customerBuilder.setFirstName("John");
    customerBuilder.setLastName("Doe");
    customerBuilder.setHeight(175.5f);
    customerBuilder.setWeight(80.5f);
    customerBuilder.setAutomatedEmail(false);
    Customer customer = customerBuilder.build();
    System.out.println(customer);

    // Write Specific Record to an AVRO file (binary format)
    final DatumWriter<Customer> writer = new SpecificDatumWriter<Customer>(Customer.class);
    try {
      // Open file writer
      DataFileWriter<Customer> dataFileWriter = new DataFileWriter<Customer>(writer);

      // Add data
      dataFileWriter.create(customer.getSchema(), new File("customer-specific.avro"));
      dataFileWriter.append(customer);
      System.out.println("File Written (customer-specific.avro)");

      // Close file writer
      dataFileWriter.close();
    } catch (IOException e){
      System.out.println("Couldn't write file");
      e.printStackTrace();
    }

    // Read Specific Record from AVRO file (binary format)
    final File file = new File("customer-specific.avro");
    final DatumReader<Customer> reader = new SpecificDatumReader<Customer>(Customer.class);
    try {
      // Open file reader
      final DataFileReader<Customer> dataFileReader = new DataFileReader<Customer>(file, reader);
      
      while (dataFileReader.hasNext()) {
        Customer readCustomer = dataFileReader.next();
        System.out.println("Reading specific record");
        System.out.println(readCustomer.toString());
        System.out.println("First name: " + readCustomer.getFirstName());
      }

      // Close file reader
      dataFileReader.close();

    } catch (IOException e) {
      e.printStackTrace();
    }


    // note, we can read our other customer generated using the generic method!
    // // end of the day, no matter the method, Avro is Avro!
    // final File fileGeneric = new File("customer-generic.avro");
    // final DatumReader<Customer> datumReaderGeneric = new SpecificDatumReader<>(Customer.class);
    // final DataFileReader<Customer> dataFileReaderGeneric;
    // try {
    //     System.out.println("Reading our specific record");
    //     dataFileReaderGeneric = new DataFileReader<>(fileGeneric, datumReaderGeneric);
    //     while (dataFileReaderGeneric.hasNext()) {
    //         Customer readCustomer = dataFileReaderGeneric.next();
    //         System.out.println(readCustomer.toString());
    //     }
    // } catch (IOException e) {
    //     e.printStackTrace();
    // }



    // Interpret

  }
}
