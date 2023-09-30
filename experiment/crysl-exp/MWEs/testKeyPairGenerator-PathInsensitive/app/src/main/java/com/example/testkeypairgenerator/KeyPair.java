package com.example.testkeypairgenerator;

import java.math.BigInteger;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.interfaces.RSAPublicKey;

class KeyPairWrapper {
    private KeyPairGenerator keyPairGen;
    BigInteger n;
    byte[] n_array;

    //new a RSA keyPairGen
    public void init() throws Exception {
        this.keyPairGen = KeyPairGenerator.getInstance("RSA");
    }

    // get RSAPublicKey modulus
    public byte[] getModulus() throws Exception {
        if (this.n == null) {
            this.keyPairGen.initialize(2048);
            KeyPair keyPair = keyPairGen.generateKeyPair();
            this.n = ((RSAPublicKey) keyPair.getPublic()).getModulus();
            return this.n.toByteArray();
        }
        return this.n_array;
    }
}
