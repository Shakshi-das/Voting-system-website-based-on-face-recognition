package com.collegeproject.backendandfrontend.Controller;

import java.util.HashMap;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.collegeproject.backendandfrontend.Model.voter;
import com.collegeproject.backendandfrontend.Service.VoterService;




@RestController
public class VoteController {

     @Autowired
    private VoterService voterService;

    
    @PostMapping("register")
    public ResponseEntity<Map<String, String>> registerVoter(@RequestBody voter voter) 
    {
        String result = voterService.registerVoter(voter);
        Map<String, String> response = new HashMap<>();
        response.put("message", result);
        return ResponseEntity.ok(response);
    }


    @PostMapping("login")
    public ResponseEntity<Map<String, String>> loginVoter(@RequestBody Map<String, String> loginData) 
    {
        String voterId = loginData.get("voterId");
        String password = loginData.get("password");
        String faceImage = loginData.get("faceImage");

        String result = voterService.loginVoter(voterId, password, faceImage);

        Map<String, String> response = new HashMap<>();
        response.put("message", result);
        return ResponseEntity.ok(response);
    }


    // Voting endpoint
    @PostMapping("vote")
    public String castVote(@RequestParam String voterId, @RequestParam String candidate) 
    {
        return voterService.castVote(voterId, candidate);
    }

    @GetMapping("/vote-counts")
    public Map<String, Long> getVoteCounts() {
        return voterService.getVoteCounts();
    }

    
    

    
}
