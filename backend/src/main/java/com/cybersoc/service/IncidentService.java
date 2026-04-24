package com.cybersoc.service;

import com.cybersoc.model.Incident;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class IncidentService {
    private final List<Incident> incidents = new ArrayList<>();

    public Incident createIncident(Incident incident) {
        incidents.add(incident);
        return incident;
    }

    public List<Incident> getAllIncidents() {
        return incidents;
    }

    public Optional<Incident> getIncidentById(Long id) {
        return incidents.stream().filter(incident -> incident.getId().equals(id)).findFirst();
    }

    public Incident updateIncident(Long id, Incident updatedIncident) {
        Incident incident = getIncidentById(id).orElseThrow(() -> new RuntimeException("Incident not found"));
        incident.setTitle(updatedIncident.getTitle());
        incident.setDescription(updatedIncident.getDescription());
        // Set other fields as necessary
        return incident;
    }

    public void deleteIncident(Long id) {
        incidents.removeIf(incident -> incident.getId().equals(id));
    }
}