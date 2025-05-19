package com.collegeproject.backendandfrontend.Repository;

import com.collegeproject.backendandfrontend.Model.voterEntity;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface VoterRepository extends JpaRepository<voterEntity, String> {
    voterEntity findByVoterId(String voterId);
}

