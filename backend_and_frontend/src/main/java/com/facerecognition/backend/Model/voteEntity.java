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
@Table(name ="Polled_Vote_Details")
public class voteEntity {
    
    @Id
    private String voterId;
    private String candidate;
}
