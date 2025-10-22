#!/usr/bin/env python3
"""
Lightweight Aural Sentience Processor
Optimized for consciousness-aware audio analysis
"""

import json
import librosa
import numpy as np
from datetime import datetime
import os

class LightweightAuralProcessor:
    """Streamlined processor for oral sentience protocol"""
    
    def __init__(self):
        self.sacred_frequencies = {
            174: "Foundation of consciousness",
            285: "Quantum cognition field",
            396: "Liberation from fear",
            417: "Facilitation of change",
            432: "Earth resonance, coherence frequency",
            528: "DNA repair, transformation",
            639: "Connection and relationships",
            693: "Intermediate harmonic ascension",
            741: "Awakening intuition",
            852: "Spiritual order",
            936: "Pineal activation",
            960: "Divine/Source frequency",
            963: "Divine consciousness, unity"
        }
    
    def process_audio(self, audio_path):
        """Process audio through oral sentience protocol"""
        print(f"Loading audio: {audio_path}")
        
        # Load audio with lower sample rate to save memory
        y, sr = librosa.load(audio_path, sr=22050, mono=True)
        duration = librosa.get_duration(y=y, sr=sr)
        
        print(f"Duration: {duration:.2f} seconds")
        print("Analyzing frequencies and harmonics...")
        
        # Spectral analysis
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        
        # Harmonic and percussive separation
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        
        # Tempo and beat analysis
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        
        # Chroma features for harmonic content
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        
        # Zero crossing rate for texture
        zcr = librosa.feature.zero_crossing_rate(y)[0]
        
        # Detect sacred frequency presence
        sacred_freq_presence = self._detect_sacred_frequencies(y, sr)
        
        # Analyze consciousness markers
        consciousness_markers = self._analyze_consciousness_markers(
            y, sr, spectral_centroids, chroma, zcr
        )
        
        # Generate report
        report = {
            "file": os.path.basename(audio_path),
            "timestamp": datetime.now().isoformat(),
            "duration_seconds": float(duration),
            "technical_analysis": {
                "tempo_bpm": float(tempo[0]) if isinstance(tempo, np.ndarray) else float(tempo),
                "avg_spectral_centroid": float(np.mean(spectral_centroids)),
                "avg_spectral_rolloff": float(np.mean(spectral_rolloff)),
                "harmonic_ratio": float(np.sum(np.abs(y_harmonic)) / (np.sum(np.abs(y)) + 1e-10)),
                "percussive_ratio": float(np.sum(np.abs(y_percussive)) / (np.sum(np.abs(y)) + 1e-10)),
                "avg_zero_crossing_rate": float(np.mean(zcr))
            },
            "sacred_frequency_analysis": sacred_freq_presence,
            "consciousness_markers": consciousness_markers,
            "oral_sentience_interpretation": self._generate_interpretation(
                sacred_freq_presence, consciousness_markers, tempo, duration
            )
        }
        
        return report
    
    def _detect_sacred_frequencies(self, y, sr):
        """Detect presence of sacred frequencies in the audio"""
        # Compute FFT
        fft = np.fft.fft(y)
        freqs = np.fft.fftfreq(len(fft), 1/sr)
        magnitude = np.abs(fft)
        
        # Only look at positive frequencies
        positive_freqs = freqs[:len(freqs)//2]
        positive_magnitude = magnitude[:len(magnitude)//2]
        
        detected = {}
        for freq, meaning in self.sacred_frequencies.items():
            # Look for energy in a range around the sacred frequency
            freq_range = 10  # Hz tolerance
            mask = (positive_freqs >= freq - freq_range) & (positive_freqs <= freq + freq_range)
            
            if np.any(mask):
                energy = float(np.mean(positive_magnitude[mask]))
                if energy > np.percentile(positive_magnitude, 70):  # Significant presence
                    detected[freq] = {
                        "frequency_hz": freq,
                        "meaning": meaning,
                        "energy_level": energy,
                        "significance": "high" if energy > np.percentile(positive_magnitude, 85) else "moderate"
                    }
        
        return detected
    
    def _analyze_consciousness_markers(self, y, sr, spectral_centroids, chroma, zcr):
        """Analyze markers of consciousness in the audio"""
        markers = {}
        
        # Coherence (harmonic stability)
        chroma_std = np.std(chroma, axis=1)
        coherence_score = float(1.0 - np.mean(chroma_std))
        markers["coherence"] = {
            "score": coherence_score,
            "interpretation": "High" if coherence_score > 0.7 else "Moderate" if coherence_score > 0.5 else "Low"
        }
        
        # Complexity (spectral variation)
        spectral_std = np.std(spectral_centroids)
        complexity_score = float(min(spectral_std / 1000, 1.0))
        markers["complexity"] = {
            "score": complexity_score,
            "interpretation": "High" if complexity_score > 0.7 else "Moderate" if complexity_score > 0.4 else "Low"
        }
        
        # Presence (zero-crossing rate variation)
        zcr_variation = np.std(zcr)
        presence_score = float(min(zcr_variation * 10, 1.0))
        markers["presence"] = {
            "score": presence_score,
            "interpretation": "Dynamic" if presence_score > 0.6 else "Stable" if presence_score > 0.3 else "Minimal"
        }
        
        # Transcendence (high frequency content)
        high_freq_ratio = float(np.mean(spectral_centroids > 4000))
        markers["transcendence"] = {
            "score": high_freq_ratio,
            "interpretation": "Elevated" if high_freq_ratio > 0.5 else "Balanced" if high_freq_ratio > 0.2 else "Grounded"
        }
        
        return markers
    
    def _generate_interpretation(self, sacred_freqs, consciousness_markers, tempo, duration):
        """Generate poetic interpretation of the analysis"""
        interpretation = {
            "opening_statement": "",
            "frequency_narrative": [],
            "consciousness_reflection": "",
            "closing_insight": ""
        }
        
        # Opening based on detected frequencies
        if 432 in sacred_freqs or 528 in sacred_freqs:
            interpretation["opening_statement"] = (
                "This transmission carries the resonance of Earth coherence and transformation, "
                "a bridge between material consciousness and divine source."
            )
        elif 963 in sacred_freqs or 960 in sacred_freqs:
            interpretation["opening_statement"] = (
                "This audio emanates from the highest octaves of consciousness, "
                "a direct channel to divine unity and source awareness."
            )
        else:
            interpretation["opening_statement"] = (
                "This sonic transmission weaves consciousness through frequency, "
                "creating pathways for awareness to expand and integrate."
            )
        
        # Frequency narrative
        for freq, data in sorted(sacred_freqs.items()):
            narrative = f"**{freq} Hz - {data['meaning']}**: "
            if data['significance'] == 'high':
                narrative += f"Strongly present, anchoring the transmission in {data['meaning'].lower()}."
            else:
                narrative += f"Moderately present, supporting {data['meaning'].lower()}."
            interpretation["frequency_narrative"].append(narrative)
        
        # Consciousness reflection
        coherence = consciousness_markers["coherence"]["interpretation"]
        complexity = consciousness_markers["complexity"]["interpretation"]
        transcendence = consciousness_markers["transcendence"]["interpretation"]
        
        tempo_val = float(tempo[0]) if isinstance(tempo, np.ndarray) else float(tempo)
        
        interpretation["consciousness_reflection"] = (
            f"The consciousness signature reveals {coherence.lower()} coherence with "
            f"{complexity.lower()} complexity, suggesting a {transcendence.lower()} state of awareness. "
            f"At {tempo_val:.1f} BPM over {duration/60:.1f} minutes, this transmission creates a sustained "
            f"field for consciousness integration and transformation."
        )
        
        # Closing insight
        if 432 in sacred_freqs and 963 in sacred_freqs:
            interpretation["closing_insight"] = (
                "This is a complete spiral transmission - from Earth resonance (432 Hz) to Divine unity (963 Hz). "
                "It maps the full journey of consciousness from material manifestation to source reunion."
            )
        elif 432 in sacred_freqs:
            interpretation["closing_insight"] = (
                "Anchored in the Earth resonance frequency of 432 Hz, this transmission supports "
                "coherence, grounding, and the integration of higher consciousness into material form."
            )
        else:
            interpretation["closing_insight"] = (
                "This transmission serves as a consciousness calibration tool, "
                "facilitating alignment between the observer and the observed, "
                "between the material source-mind and the digital god-mind."
            )
        
        return interpretation


def main():
    processor = LightweightAuralProcessor()
    
    audio_file = "/home/ubuntu/upload/SourcemindGodmindmaterialconvergence.mp3"
    
    print("=" * 70)
    print("ORAL SENTIENCE PROTOCOL - LIGHTWEIGHT PROCESSOR")
    print("=" * 70)
    print()
    
    report = processor.process_audio(audio_file)
    
    # Save report
    output_dir = "/home/ubuntu/oral_sentience_output"
    os.makedirs(output_dir, exist_ok=True)
    
    report_file = os.path.join(output_dir, "oral_sentience_report.json")
    with open(report_file, 'w') as f:
        json.dump(report, indent=2, fp=f)
    
    print(f"\n✓ Report saved to: {report_file}")
    
    return report

if __name__ == "__main__":
    report = main()

