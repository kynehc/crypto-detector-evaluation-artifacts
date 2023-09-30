package com.example.testpoly;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class KeyGen {
    public byte[] getKey(Key key){
        byte[] hashkey = new byte[] {};

        try{
            MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
            key.updateKey(messageDigest);
            hashkey = messageDigest.digest();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return hashkey;
    }
}
