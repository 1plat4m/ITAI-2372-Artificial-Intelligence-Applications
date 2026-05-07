import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

# Create directory for images
output_dir = "agi_healthcare_graphics"
os.makedirs(output_dir, exist_ok=True)

def create_graphic_1():
    # Graphic 1: Narrow AI vs AGI Comparison
    fig, ax = plt.subplots(figsize=(7, 7), dpi=100)
    fig.patch.set_facecolor('#f0f4f8')
    ax.axis('off')
    
    plt.text(0.5, 0.92, "Narrow AI vs. AGI", ha='center', fontsize=20, weight='bold', color='#1a365d')
    plt.text(0.5, 0.86, "The Shift in Healthcare Intelligence", ha='center', fontsize=12, color='#2d3748')

    # Left Side: Narrow AI
    rect1 = patches.FancyBboxPatch((0.05, 0.2), 0.4, 0.6, linewidth=2, edgecolor='#e53e3e', facecolor='white', boxstyle="round,pad=0.05")
    ax.add_patch(rect1)
    plt.text(0.25, 0.75, "NARROW AI", ha='center', fontsize=14, weight='bold', color='#e53e3e')
    plt.text(0.25, 0.65, "Task Specific", ha='center', fontsize=10, weight='bold')
    items_narrow = ["• Reading Scans", "• Predicting Sepsis", "• Voice Dictation", "• SQL Queries"]
    for i, item in enumerate(items_narrow):
        plt.text(0.1, 0.55 - (i*0.06), item, fontsize=10, color='#4a5568')

    # Right Side: AGI
    rect2 = patches.FancyBboxPatch((0.55, 0.2), 0.4, 0.6, linewidth=2, edgecolor='#3182ce', facecolor='white', boxstyle="round,pad=0.05")
    ax.add_patch(rect2)
    plt.text(0.75, 0.75, "AGI", ha='center', fontsize=14, weight='bold', color='#3182ce')
    plt.text(0.75, 0.65, "Reasoning & Synthesis", ha='center', fontsize=10, weight='bold')
    items_agi = ["• Holistic Diagnosis", "• Genomic History", "• Socioeconomic Data", "• Lifestyle Context"]
    for i, item in enumerate(items_agi):
        plt.text(0.6, 0.55 - (i*0.06), item, fontsize=10, color='#4a5568')

    plt.arrow(0.46, 0.5, 0.06, 0, head_width=0.03, head_length=0.02, fc='#2d3748', ec='#2d3748')
    plt.savefig(f"{output_dir}/comparison_chart.png", bbox_inches='tight', pad_inches=0.2)
    plt.close()

def create_graphic_2():
    # Graphic 2: The Super-Consultant Workflow
    fig, ax = plt.subplots(figsize=(7, 7), dpi=100)
    fig.patch.set_facecolor('#f7fafc')
    ax.axis('off')

    plt.text(0.5, 0.9, "The 'Super-Consultant' AGI", ha='center', fontsize=18, weight='bold', color='#2c5282')
    
    # Central Node
    circle = patches.Circle((0.5, 0.5), 0.15, color='#4299e1', alpha=0.8)
    ax.add_patch(circle)
    plt.text(0.5, 0.5, "AGI\nENGINE", ha='center', va='center', color='white', weight='bold', fontsize=14)

    # Input Nodes
    inputs = [
        (0.2, 0.75, "Wearable Data"),
        (0.8, 0.75, "Genomic Seq"),
        (0.2, 0.25, "Medical Lit"),
        (0.8, 0.25, "Digital Twin")
    ]
    
    for x, y, label in inputs:
        c = patches.Circle((x, y), 0.1, color='white', ec='#4299e1', lw=2)
        ax.add_patch(c)
        plt.text(x, y, label, ha='center', va='center', fontsize=9, weight='bold', color='#2d3748')
        plt.annotate('', xy=(0.5, 0.5), xytext=(x, y), arrowprops=dict(arrowstyle='<-', color='#a0aec0', lw=1.5))

    plt.text(0.5, 0.1, "Autonomous Cross-Modal Synthesis", ha='center', fontsize=11, style='italic', color='#718096')
    plt.savefig(f"{output_dir}/super_consultant.png", bbox_inches='tight', pad_inches=0.2)
    plt.close()

def create_graphic_3():
    # Graphic 3: Benefits vs Risks Infographic
    fig, ax = plt.subplots(figsize=(7, 7), dpi=100)
    fig.patch.set_facecolor('#fffaf0')
    ax.axis('off')

    plt.text(0.5, 0.92, "The AGI Impact Matrix", ha='center', fontsize=20, weight='bold', color='#744210')

    # Benefits Box
    ax.add_patch(patches.Rectangle((0.1, 0.52), 0.8, 0.3, color='#f0fff4', ec='#38a169', lw=2))
    plt.text(0.15, 0.78, "ANTICIPATED BENEFITS", fontsize=13, weight='bold', color='#2f855a')
    benefits = ["+ Universal Access (Expertise for all)", "+ Hyper-Personalized Treatments", "+ Discovery of New Drug Compounds"]
    for i, b in enumerate(benefits):
        plt.text(0.15, 0.7 - (i*0.06), b, fontsize=11, color='#2d3748')

    # Risks Box
    ax.add_patch(patches.Rectangle((0.1, 0.15), 0.8, 0.3, color='#fff5f5', ec='#e53e3e', lw=2))
    plt.text(0.15, 0.41, "RISKS & ETHICAL CONCERNS", fontsize=13, weight='bold', color='#c53030')
    risks = ["- The Black Box (Traceability)", "- Scaled Algorithmic Bias", "- De-skilling of Human Clinicians"]
    for i, r in enumerate(risks):
        plt.text(0.15, 0.33 - (i*0.06), r, fontsize=11, color='#2d3748')

    plt.savefig(f"{output_dir}/impact_matrix.png", bbox_inches='tight', pad_inches=0.2)
    plt.close()

# Generate all images
create_graphic_1()
create_graphic_2()
create_graphic_3()