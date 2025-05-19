package com.collegeproject.backendandfrontend.Service;

import java.util.Map;

import com.collegeproject.backendandfrontend.Model.voter;

public interface VoterService {
    
    String registerVoter(voter voter);
    String loginVoter(String voterId, String password, String faceImage);
    String castVote(String voterId, String candidate) ;
     Map<String, Long> getVoteCounts();
    
}
