package com.cybersoc.repository;

import com.cybersoc.entity.Incident;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface IncidentRepository extends JpaRepository<Incident, Long> {
    List<Incident> findBySeverity(String severity);
    List<Incident> findByStatus(String status);
    List<Incident> findByAssignedTo(Long assignedTo);
}