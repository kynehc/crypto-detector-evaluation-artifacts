package com.example.testpoly;

import java.security.MessageDigest;

public interface Key {
    void updateKey(MessageDigest messageDigest) throws Exception;
}
