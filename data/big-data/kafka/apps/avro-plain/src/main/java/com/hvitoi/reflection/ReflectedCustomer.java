package com.hvitoi.reflection;

import org.apache.avro.reflect.Nullable;

// PoJo - Plain Old Java Object
public class ReflectedCustomer {

    private String firstName;
    private String lastName;
    @Nullable private String nickName; // Avro Union (Complex Type): Null or String

    public ReflectedCustomer(){}

    public ReflectedCustomer(String firstName, String lastName, String nickName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.nickName = nickName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String fullName(){
        return this.firstName + " " + this.lastName + " " + this.nickName;
    }

    public String getNickName() {
        return nickName;
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }
}
