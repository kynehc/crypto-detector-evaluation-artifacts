package com.example.testpoly;

import java.security.MessageDigest;

public class NoUpdateKey implements Key{

    @Override
    public void updateKey(MessageDigest messageDigest) throws Exception {
        //do nothing
    }
}
