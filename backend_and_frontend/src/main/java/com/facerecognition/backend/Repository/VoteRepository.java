


package com.collegeproject.backendandfrontend.Repository;

import com.collegeproject.backendandfrontend.Model.voteEntity;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
@Repository
public interface VoteRepository extends JpaRepository<voteEntity, String> {
    voteEntity findByVoterId(String voterId);
}
