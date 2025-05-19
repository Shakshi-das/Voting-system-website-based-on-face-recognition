package com.collegeproject.backendandfrontend.Service;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.collegeproject.backendandfrontend.Model.voteEntity;
import com.collegeproject.backendandfrontend.Model.voter;
import com.collegeproject.backendandfrontend.Model.voterEntity;
import com.collegeproject.backendandfrontend.Repository.VoteRepository;
import com.collegeproject.backendandfrontend.Repository.VoterRepository;

@Service
public class VoterServiceIMP implements VoterService {
    
   @Autowired
    private VoterRepository voterRepository;

    @Autowired
    private VoteRepository voteRepository;
    
    @Override
    public String registerVoter(voter voter) {
        voterEntity CurVoter =new voterEntity();
        BeanUtils.copyProperties(voter, CurVoter);
        if (voterRepository.findByVoterId(CurVoter.getVoterId())!= null) {
            return "Voter ID already exists!";
        }
        voterRepository.save(CurVoter);
        return "Registration successful!";
    }

    @Override
    public String loginVoter(String voterId, String password, String faceImage) {
            voterEntity CurVoter = voterRepository.findByVoterId(voterId);
            if (CurVoter == null) {
                return "Voter not found!";
            }
            if (!CurVoter.getPassword().equals(password)) {
                return "Invalid password!";
            }
            // Optionally: Add face recognition check here
            return "Login successfull!";
        
        
    }

    
    @Override
    public String castVote(String voterId, String candidate) 
    {

        // Check if voter exists
        voterEntity curVoter = voterRepository.findByVoterId(voterId);
        if (curVoter == null) {
            return "Voter not found!";
        }

        // Check if voter has already voted
        if (curVoter.isHasVoted() || voteRepository.findByVoterId(voterId) != null) {
            return "You have already voted!";
        }

        // Record the new vote
        voteEntity curVote = new voteEntity();
        curVote.setVoterId(voterId);
        curVote.setCandidate(candidate);
        voteRepository.save(curVote);

        // Update voter's hasVoted status
        curVoter.setHasVoted(true);
        voterRepository.save(curVoter);

        return "Vote recorded successfully!";
    }

    @Override
    public Map<String, Long> getVoteCounts() {
    List<voteEntity> allVotes = voteRepository.findAll();
    Map<String, Long> voteCountMap = allVotes.stream()
        .collect(Collectors.groupingBy(voteEntity::getCandidate, Collectors.counting()));
    return voteCountMap;
    }


}
