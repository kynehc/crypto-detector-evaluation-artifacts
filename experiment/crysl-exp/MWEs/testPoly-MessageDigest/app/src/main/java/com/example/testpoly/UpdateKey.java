package com.example.testpoly;

import android.util.Log;

import java.security.MessageDigest;

public class UpdateKey implements Key {
    private String key = "keydata";

    @Override
    public void updateKey(MessageDigest messageDigest) throws Exception {
        byte[] data = this.key.getBytes("UTF-8");
        messageDigest.update(data);
    }
}
