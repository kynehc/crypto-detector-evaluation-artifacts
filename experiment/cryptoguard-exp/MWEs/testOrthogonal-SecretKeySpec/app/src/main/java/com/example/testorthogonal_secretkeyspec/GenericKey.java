package com.example.testorthogonal_secretkeyspec;

public class GenericKey {
    private String algorithmIdentifier;
    private Object representation;

    public GenericKey(String algorithmIdentifier, byte[] bArr) {
        this.algorithmIdentifier = algorithmIdentifier;
        this.representation = bArr;
    }

    public String getAlgorithmIdentifier() {
        return this.algorithmIdentifier;
    }

    public Object getRepresentation() {
        return this.representation;
    }
}
