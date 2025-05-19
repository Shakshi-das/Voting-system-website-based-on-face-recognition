package com.collegeproject.backendandfrontend.Model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name ="AllVoter_Details")
public class voterEntity {
    
    @Id
    private String voterId;
    private String name;
    private String password;
    private String faceImage;
    private boolean hasVoted;
}
