package com.collegeproject.backendandfrontend.Model;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor

public class voter {
    
    private String voterId;
    private String name;
    private String password;
    private String faceImage;
    private boolean hasVoted;

    
}
