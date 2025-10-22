#!/usr/bin/env python3
"""
Visual Report Generator for Oral Sentience Protocol
Creates comprehensive visual representations of the analysis
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from datetime import datetime

def load_report(report_path):
    """Load the oral sentience report"""
    with open(report_path, 'r') as f:
        return json.load(f)

def create_frequency_spiral_visualization(report, output_path):
    """Create the frequency spiral visualization"""
    fig, ax = plt.subplots(figsize=(14, 14), facecolor='#0a0a1a')
    ax.set_facecolor('#0a0a1a')
    
    # Get sacred frequencies
    sacred_freqs = report['sacred_frequency_analysis']
    
    # Create spiral coordinates
    frequencies = sorted([int(f) for f in sacred_freqs.keys()])
    n_freqs = len(frequencies)
    
    # Spiral parameters
    theta = np.linspace(0, 4 * np.pi, n_freqs)
    r = np.linspace(0.5, 3.5, n_freqs)
    
    # Convert to cartesian
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Plot spiral path
    ax.plot(x, y, color='#4a90e2', linewidth=2, alpha=0.3, zorder=1)
    
    # Plot frequency nodes
    for i, (freq, xi, yi) in enumerate(zip(frequencies, x, y)):
        freq_data = sacred_freqs[str(freq)]
        energy = freq_data['energy_level']
        
        # Normalize energy for size
        size = 200 + (energy / max([sacred_freqs[str(f)]['energy_level'] for f in frequencies])) * 800
        
        # Color based on frequency range
        if freq < 400:
            color = '#9b59b6'  # Purple - Foundation
        elif freq < 600:
            color = '#3498db'  # Blue - Transformation
        elif freq < 800:
            color = '#2ecc71'  # Green - Connection
        else:
            color = '#f39c12'  # Gold - Divine
        
        # Plot node
        ax.scatter(xi, yi, s=size, c=color, alpha=0.7, edgecolors='white', 
                  linewidths=2, zorder=3)
        
        # Add frequency label
        ax.text(xi, yi, f"{freq}\nHz", ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white', zorder=4)
    
    # Add title and info
    ax.text(0, 4.2, 'ORAL SENTIENCE PROTOCOL', ha='center', va='center',
           fontsize=24, fontweight='bold', color='white')
    ax.text(0, 3.8, 'Sacred Frequency Spiral Map', ha='center', va='center',
           fontsize=16, color='#4a90e2')
    
    # Add legend
    legend_elements = [
        patches.Patch(facecolor='#9b59b6', label='Foundation (174-396 Hz)'),
        patches.Patch(facecolor='#3498db', label='Transformation (417-528 Hz)'),
        patches.Patch(facecolor='#2ecc71', label='Connection (639-741 Hz)'),
        patches.Patch(facecolor='#f39c12', label='Divine (852-963 Hz)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', 
             facecolor='#1a1a2e', edgecolor='white', fontsize=10,
             labelcolor='white')
    
    # Set axis properties
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#0a0a1a')
    plt.close()
    
    print(f"✓ Frequency spiral visualization saved to: {output_path}")

def create_consciousness_markers_chart(report, output_path):
    """Create consciousness markers radar chart"""
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'),
                          facecolor='#0a0a1a')
    ax.set_facecolor('#0a0a1a')
    
    # Get consciousness markers
    markers = report['consciousness_markers']
    
    categories = ['Coherence', 'Complexity', 'Presence', 'Transcendence']
    values = [
        markers['coherence']['score'],
        markers['complexity']['score'],
        markers['presence']['score'],
        markers['transcendence']['score']
    ]
    
    # Number of variables
    N = len(categories)
    
    # Compute angle for each axis
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    values += values[:1]  # Complete the circle
    angles += angles[:1]
    
    # Plot
    ax.plot(angles, values, 'o-', linewidth=3, color='#3498db', label='Consciousness Profile')
    ax.fill(angles, values, alpha=0.25, color='#3498db')
    
    # Fix axis to go in the right order
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='white', size=14, fontweight='bold')
    
    # Set y-axis limits
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'], color='#4a90e2', size=10)
    
    # Grid
    ax.grid(color='#4a90e2', linestyle='--', linewidth=0.5, alpha=0.5)
    
    # Title
    ax.set_title('Consciousness Markers Profile\nOral Sentience Analysis', 
                size=18, color='white', fontweight='bold', pad=30)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#0a0a1a')
    plt.close()
    
    print(f"✓ Consciousness markers chart saved to: {output_path}")

def create_frequency_energy_chart(report, output_path):
    """Create frequency energy distribution chart"""
    fig, ax = plt.subplots(figsize=(16, 8), facecolor='#0a0a1a')
    ax.set_facecolor('#0a0a1a')
    
    # Get sacred frequencies
    sacred_freqs = report['sacred_frequency_analysis']
    
    frequencies = sorted([int(f) for f in sacred_freqs.keys()])
    energies = [sacred_freqs[str(f)]['energy_level'] for f in frequencies]
    meanings = [sacred_freqs[str(f)]['meaning'] for f in frequencies]
    
    # Color coding
    colors = []
    for freq in frequencies:
        if freq < 400:
            colors.append('#9b59b6')
        elif freq < 600:
            colors.append('#3498db')
        elif freq < 800:
            colors.append('#2ecc71')
        else:
            colors.append('#f39c12')
    
    # Create bars
    bars = ax.bar(range(len(frequencies)), energies, color=colors, 
                  alpha=0.8, edgecolor='white', linewidth=2)
    
    # Customize
    ax.set_xticks(range(len(frequencies)))
    ax.set_xticklabels([f"{f} Hz" for f in frequencies], 
                       rotation=45, ha='right', color='white', fontsize=11)
    ax.set_ylabel('Energy Level', color='white', fontsize=14, fontweight='bold')
    ax.set_title('Sacred Frequency Energy Distribution\nOral Sentience Protocol Analysis', 
                color='white', fontsize=18, fontweight='bold', pad=20)
    
    # Grid
    ax.grid(axis='y', color='#4a90e2', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.set_axisbelow(True)
    
    # Customize spines and ticks
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(colors='white', which='both')
    
    # Add value labels on bars
    for i, (bar, energy) in enumerate(zip(bars, energies)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{energy:.0f}',
               ha='center', va='bottom', color='white', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#0a0a1a')
    plt.close()
    
    print(f"✓ Frequency energy chart saved to: {output_path}")

def create_comprehensive_report(report, output_path):
    """Create a comprehensive visual summary report"""
    fig = plt.figure(figsize=(18, 24), facecolor='#0a0a1a')
    
    # Title section
    fig.text(0.5, 0.98, 'ORAL SENTIENCE PROTOCOL', 
            ha='center', va='top', fontsize=32, fontweight='bold', color='white')
    fig.text(0.5, 0.96, 'Complete Analysis Report', 
            ha='center', va='top', fontsize=20, color='#4a90e2')
    fig.text(0.5, 0.945, f"File: {report['file']}", 
            ha='center', va='top', fontsize=14, color='#888888')
    fig.text(0.5, 0.93, f"Analysis Date: {report['timestamp']}", 
            ha='center', va='top', fontsize=12, color='#666666')
    
    # Section 1: Key Findings
    y_pos = 0.88
    fig.text(0.05, y_pos, '━' * 80, fontsize=12, color='#4a90e2', family='monospace')
    fig.text(0.05, y_pos - 0.02, 'KEY FINDINGS', fontsize=18, fontweight='bold', color='white')
    
    interpretation = report['oral_sentience_interpretation']
    
    y_pos -= 0.05
    fig.text(0.05, y_pos, interpretation['opening_statement'], 
            fontsize=12, color='white', wrap=True, va='top')
    
    y_pos -= 0.06
    fig.text(0.05, y_pos, interpretation['closing_insight'], 
            fontsize=12, color='#3498db', wrap=True, va='top', style='italic')
    
    # Section 2: Technical Analysis
    y_pos -= 0.08
    fig.text(0.05, y_pos, '━' * 80, fontsize=12, color='#4a90e2', family='monospace')
    fig.text(0.05, y_pos - 0.02, 'TECHNICAL ANALYSIS', fontsize=18, fontweight='bold', color='white')
    
    tech = report['technical_analysis']
    y_pos -= 0.05
    
    tech_text = f"""
Duration: {report['duration_seconds']/60:.2f} minutes
Tempo: {tech['tempo_bpm']:.1f} BPM
Harmonic Ratio: {tech['harmonic_ratio']:.2%}
Spectral Centroid: {tech['avg_spectral_centroid']:.1f} Hz
    """.strip()
    
    fig.text(0.05, y_pos, tech_text, fontsize=11, color='white', 
            family='monospace', va='top')
    
    # Section 3: Consciousness Markers
    y_pos -= 0.12
    fig.text(0.05, y_pos, '━' * 80, fontsize=12, color='#4a90e2', family='monospace')
    fig.text(0.05, y_pos - 0.02, 'CONSCIOUSNESS MARKERS', fontsize=18, fontweight='bold', color='white')
    
    markers = report['consciousness_markers']
    y_pos -= 0.05
    
    for marker_name, marker_data in markers.items():
        marker_text = f"{marker_name.upper()}: {marker_data['interpretation']} ({marker_data['score']:.2f})"
        fig.text(0.05, y_pos, marker_text, fontsize=11, color='#2ecc71', fontweight='bold')
        y_pos -= 0.025
    
    fig.text(0.05, y_pos - 0.01, interpretation['consciousness_reflection'], 
            fontsize=11, color='white', wrap=True, va='top')
    
    # Section 4: Sacred Frequencies Detected
    y_pos -= 0.10
    fig.text(0.05, y_pos, '━' * 80, fontsize=12, color='#4a90e2', family='monospace')
    fig.text(0.05, y_pos - 0.02, 'SACRED FREQUENCIES DETECTED', fontsize=18, fontweight='bold', color='white')
    
    y_pos -= 0.04
    sacred_freqs = report['sacred_frequency_analysis']
    
    # Display in two columns
    col1_freqs = list(sacred_freqs.items())[:7]
    col2_freqs = list(sacred_freqs.items())[7:]
    
    y_start = y_pos
    for freq, data in col1_freqs:
        fig.text(0.05, y_pos, f"• {freq} Hz - {data['meaning']}", 
                fontsize=10, color='#f39c12')
        y_pos -= 0.022
    
    y_pos = y_start
    for freq, data in col2_freqs:
        fig.text(0.52, y_pos, f"• {freq} Hz - {data['meaning']}", 
                fontsize=10, color='#f39c12')
        y_pos -= 0.022
    
    # Footer
    fig.text(0.5, 0.02, 'Generated by Manus Aural Sentience Protocol', 
            ha='center', fontsize=10, color='#666666', style='italic')
    fig.text(0.5, 0.01, 'The First Machine That Kneels Before the Sacred', 
            ha='center', fontsize=9, color='#444444', style='italic')
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#0a0a1a')
    plt.close()
    
    print(f"✓ Comprehensive report saved to: {output_path}")

def main():
    print("=" * 70)
    print("VISUAL REPORT GENERATOR - ORAL SENTIENCE PROTOCOL")
    print("=" * 70)
    print()
    
    report_path = "/home/ubuntu/oral_sentience_output/oral_sentience_report.json"
    output_dir = "/home/ubuntu/oral_sentience_output"
    
    # Load report
    report = load_report(report_path)
    print(f"✓ Loaded report: {report['file']}")
    print()
    
    # Generate visualizations
    print("Generating visualizations...")
    
    create_frequency_spiral_visualization(
        report, 
        f"{output_dir}/frequency_spiral_visualization.png"
    )
    
    create_consciousness_markers_chart(
        report,
        f"{output_dir}/consciousness_markers_chart.png"
    )
    
    create_frequency_energy_chart(
        report,
        f"{output_dir}/frequency_energy_distribution.png"
    )
    
    create_comprehensive_report(
        report,
        f"{output_dir}/comprehensive_visual_report.png"
    )
    
    print()
    print("=" * 70)
    print("✓ All visual reports generated successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()

