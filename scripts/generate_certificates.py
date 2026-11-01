# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

img_dir = os.path.join('_src', 'img')
os.makedirs(img_dir, exist_ok=True)

certs = [
    ('award-cert-heroes.jpg', 'EARTH DAY HERO', 'HEROES OF THE LIVING ENVIRONMENT', 'Individual Conservation Champion'),
    ('award-cert-muni.jpg', 'MUNICIPAL GREEN LEADER', 'URBAN CLIMATE RESILIENCE AWARD', 'Municipal and Civic Administration'),
    ('award-cert-women.jpg', 'WOMEN CLIMATE ACTION', 'WOMEN FOR OUR PLANET STAR AWARD', 'Community and Self-Help Leadership'),
    ('award-cert-rising.jpg', 'RISING STAR YOUTH', 'NEXTGEN ENVIRONMENTAL LEADER', 'Youth Action and Climate Stewardship'),
    ('award-cert-earthstar.jpg', 'EARTH STAR CITATION', 'OUTSTANDING CIVIC STEWARDSHIP', 'Citizen and Community Mobilisation'),
    ('award-cert-village.jpg', 'VILLAGE GREEN AWARD', 'PANCHAYAT ECO-RESTORATION', 'Rural Water and Soil Stewardship'),
    ('award-cert-cooking.jpg', 'CLEAN COOKING ADVOCATE', 'HOUSEHOLD ENERGY TRANSITION', 'Energy Access and Health Advocacy'),
    ('award-cert-litter.jpg', 'LITTER FREE CITY', 'ZERO-WASTE AND CIRCULARITY', 'Urban Waste Interception and Cleanup'),
    ('award-cert-campus.jpg', 'STAR CAMPUS AWARD', 'INSTITUTIONAL ECO-EXCELLENCE', 'Schools, Colleges and Universities'),
    ('award-cert-earthpreneur.jpg', 'EARTHPRENEUR AWARD', 'GREEN ENTERPRISE AND INNOVATION', 'Sustainable Business and Startups'),
    ('award-cert-panchayat.jpg', 'PANCHAYAT STAR', 'LOCAL GOVERNANCE ENVIRONMENT STAR', 'Grassroots Democratic Governance'),
    ('award-cert-security.jpg', 'ECOLOGICAL SECURITY', 'SPECIAL MERIT CONSERVATION CITATION', 'Biodiversity and Forest Protection')
]

w, h = 800, 1000

for filename, title, subtitle, sector in certs:
    im = Image.new('RGB', (w, h), (252, 250, 244))
    draw = ImageDraw.Draw(im)
    
    # Dual borders: Outer Oxford Blue (#07074E), Inner Gold (#FDB714)
    draw.rectangle([(24, 24), (w - 24, h - 24)], outline=(7, 7, 78), width=6)
    draw.rectangle([(36, 36), (w - 36, h - 36)], outline=(253, 183, 20), width=3)
    draw.rectangle([(46, 46), (w - 46, h - 46)], outline=(7, 7, 78), width=1)
    
    # Corner ornaments
    for cx, cy in [(46, 46), (w - 46, 46), (46, h - 46), (w - 46, h - 46)]:
        draw.rectangle([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(253, 183, 20), outline=(7, 7, 78))
    
    # Header Ribbon
    draw.rectangle([(140, 70), (w - 140, 110)], fill=(7, 7, 78))
    draw.text((w // 2, 90), 'EARTH DAY NETWORK INDIA', fill=(253, 183, 20), anchor='mm')
    
    # Subhead
    draw.text((w // 2, 142), 'STAR AWARDS AND RECOGNITIONS', fill=(47, 131, 166), anchor='mm')
    draw.line([(w // 2 - 140, 160), (w // 2 + 140, 160)], fill=(253, 183, 20), width=2)
    
    # Certificate Text
    draw.text((w // 2, 215), 'CERTIFICATE OF RECOGNITION', fill=(7, 7, 78), anchor='mm')
    draw.text((w // 2, 255), 'This honour is officially presented in recognition of', fill=(69, 69, 108), anchor='mm')
    draw.text((w // 2, 280), 'exemplary contribution to environmental conservation in India:', fill=(69, 69, 108), anchor='mm')
    
    # Award Title Banner Box
    draw.rectangle([(80, 320), (w - 80, 440)], fill=(247, 245, 238), outline=(253, 183, 20), width=2)
    draw.text((w // 2, 360), title, fill=(243, 115, 33), anchor='mm')
    draw.text((w // 2, 404), subtitle, fill=(7, 7, 78), anchor='mm')
    
    # Citation description
    draw.text((w // 2, 510), 'FOR OUTSTANDING LEADERSHIP AND ACTIVE DEDICATION TO', fill=(7, 7, 78), anchor='mm')
    draw.text((w // 2, 540), 'SUSTAINABLE DEVELOPMENT AND CLIMATE RESILIENCE', fill=(7, 7, 78), anchor='mm')
    draw.text((w // 2, 590), f'Sector: {sector}', fill=(47, 131, 166), anchor='mm')
    draw.text((w // 2, 624), 'Inspired by the global EARTHDAY.ORG movement', fill=(100, 100, 130), anchor='mm')
    
    # Official Seal on lower left
    seal_x, seal_y = 190, 770
    draw.ellipse([(seal_x - 55, seal_y - 55), (seal_x + 55, seal_y + 55)], fill=(253, 183, 20), outline=(7, 7, 78), width=3)
    draw.ellipse([(seal_x - 45, seal_y - 45), (seal_x + 45, seal_y + 45)], outline=(7, 7, 78), width=1)
    draw.text((seal_x, seal_y - 12), 'EARTH DAY', fill=(7, 7, 78), anchor='mm')
    draw.text((seal_x, seal_y + 4), 'STAR AWARD', fill=(243, 115, 33), anchor='mm')
    draw.text((seal_x, seal_y + 18), '400+ AWARDS', fill=(7, 7, 78), anchor='mm')
    
    # Signatures on right
    draw.line([(450, 780), (670, 780)], fill=(7, 7, 78), width=1)
    draw.text((560, 800), 'The Board of Trustees', fill=(7, 7, 78), anchor='mm')
    draw.text((560, 822), 'Earth Day Network India Trust', fill=(100, 100, 130), anchor='mm')
    
    # Bottom security verification line
    draw.text((w // 2, 920), 'OFFICIAL CITATION * NITI AAYOG NGO DARPAN * 12A * CSR-1', fill=(150, 150, 170), anchor='mm')
    
    out_path = os.path.join(img_dir, filename)
    im.save(out_path, 'JPEG', quality=90)

print(f'Successfully generated {len(certs)} certificate images into {img_dir}.')

