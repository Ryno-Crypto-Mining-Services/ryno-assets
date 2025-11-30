#!/usr/bin/env python3
"""
Script to reorganize and rename media assets according to CLAUDE.md naming conventions
"""

import shutil
from pathlib import Path

# Resolution data from identify command
resolutions = {
    "BTC-Mech.jpeg": "886x886",
    "BTC-Tree.jpeg": "886x886",
    "BTC-Sattelite.jpeg": "886x886",
    "BTC-Robot_Hand.jpeg": "886x886",
    "BTC-Jesus.png": "1024x1024",
    "TerraHash_Stack-Tech_Stack.png": "1024x1536",
    "banner-future_of_mining-300x250-v1.0-cc.png": "1024x1024",
    "banner-liquid_cooled_AI_optimized-300x250-v1.0-cc.png": "1024x1024",
    "banner-ryno_crypto_terrahash_stack-300x250-v1.0-cc.png": "1024x1024",
    "banner-ryno_mining-terrahash_stack-v1.0-cc.jpg": "1024x1024",
    "banner-sustainable_btc_mininig-300x250-v1.0-cc.png": "1024x1024",
    "banner-sustainable_scalable_mining-300x250-v1.0-cc.png": "1024x1024",
    "ryno-mining-scalable-solutions-v1.0-cc.png": "1024x1024",
    "banner-mining_evolved-160x600-v1.0-cc.png": "1024x1536",
    "ryno-mining-renewable-energy-v1.0-cc.png": "1024x1536",
    "ryno_terrahash_stack_banner-v1.0-cc.jpeg": "1086x724",
    "banner-cut_costs-728x90-v1.0-cc.png": "1536x1024",
    "banner-cut_costs-v2.0-cc.png": "1536x1024",
    "banner-ryno_terrahash_stack-v1.0-cc.png": "1536x1024",
    "ryno-terrahash-banner-v1.0-cc.jpg": "1536x1024",
    "bitcoin_mining-v1.0-cc.png": "1024x1024",
    "btc_terrahash_stack-v1.0-cc.png": "1024x1024",
    "ryno_crypto_mining_services-logo-blue-v1.0-cc.png": "1024x1024",
    "ryno_crypto-graffiti-color-v1.0-cc.png": "1024x1024",
    "ryno-logo-street_style-bw-v1.0-cc.png": "1024x1024",
    "ryno_crypto-graffiti-bw-v1.0-cc.png": "2048x2048",
    "ryno_miner_aggressive-graffiti-bw-v1.0-cc.png": "2048x2048",
    "ryno_miner_cartoon-graffiti-v1.0-cc.png": "2048x2048",
    "ryno_miner_crash-graffiti-bw-v1.0-cc.png": "2048x2048",
    "btc_terrahash_stack-512x512-v1.0-cc.png": "512x512",
    "terrahash_stack-logo-v1.0-cc.jpeg": "886x886",
    "ryno_crypto-services-v1.0-cc.jpeg": "956x1032",
    "ryno_crypto-services-v1.1-cc.png": "992x1056",
    "terrahash_infographic_1_system_architecture_v2.png": "1536x1024",
    "terrahash_infographic_2_rebalancing_process_v2.png": "1024x1536",
    "terrahash_infographic_3_dual_strategy_v2.png": "1024x1024",
    "terrahash_infographic_4_yield_generation_v2.png": "1536x1024",
    "terrahash_infographic_5_comparison_matrix_v2.png": "1536x1024",
    "ryno-mining-market-growth-v1.0-cc.png": "1600x1200",
    "terrahash_stack_features-v1.0-cc.png": "2400x1600",
    "ryno-mining-pitch-deck-v1.0.png": "4770x2670",
    "ai_liquid_cooling-v1.0-cc.png": "1536x1024",
    "terrahash_mining_facility-v1.0-cc.png": "1536x1024",
    "terrahash-lab-v1.0-cc.png": "1536x1024",
    "terrahash-liquidcooling-v1.0-cc.png": "1024x1024",
    "ryno-street_stencil-v1.0-cc.png": "1024x1024",
    "ryno-street_art-v1.0-cc.png": "2048x2048",
    "ryno-street_art-v1.1-cc.png": "2048x2048",
    "ryno-street_art-v1.2-cc.png": "2048x2048",
    "ryno-street_stencil-v1.1-cc.png": "2048x2048",
    "container_cutaway_3d_final.png": "1536x1024",
    "Wharton_Texas-facility_aerial_view.png": "1536x1024",
    "Wharton_Texas-facility_elevated.png": "1536x1024",
    "Wharton_Texas-facility_night.png": "1536x1024",
    "Wharton_Texas-facility_street_view.png": "1536x1024",
    "Screenshot 2025-10-22 at 11.00.11.png": "2934x1598",
    "Screenshot 2025-10-22 at 11.04.05.png": "3574x1658",
    "Screenshot 2025-10-22 at 11.01.34.png": "3574x1674",
    "Screenshot 2025-10-22 at 11.03.36.png": "3574x1694",
    "Screenshot 2025-10-22 at 11.01.00.png": "3574x1714",
    "ryno_head-street_style-v1.0-cc.png": "1024x1024",
    "ryno_mining-stencil-bw-v1.0-cc.png": "1024x1024",
    "ryno-mining-ai-mining-v1.0-cc.png": "1024x1024",
    "ryno_head-v1.1-cc.png": "857x665",
    "ryno-head-v1.0-cc.jpg": "857x665",
    "terrahash_ad_2_smart_dip_buying_v2.png": "1024x1024",
    "terrahash_ad_3_yield_while_wait_v2.png": "1024x1024",
    "terrahash_ad_4_price_protection_v2.png": "1024x1024",
    "terrahash_ad_5_defi_advantage_v2.png": "1024x1024",
}

# Comprehensive file mapping: (old_path, new_path)
file_mappings = [
    # Bitcoin Art
    (
        "media/Ryno Crypto Mining Marketing/Bitcoin Art/BTC-Mech.jpeg",
        "assets/images/ryno-crypto/bitcoin-art/ryno-crypto-btc-mech-art-886x886-v1-0.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Bitcoin Art/BTC-Tree.jpeg",
        "assets/images/ryno-crypto/bitcoin-art/ryno-crypto-btc-tree-art-886x886-v1-0.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Bitcoin Art/BTC-Sattelite.jpeg",
        "assets/images/ryno-crypto/bitcoin-art/ryno-crypto-btc-satellite-art-886x886-v1-0.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Bitcoin Art/BTC-Robot_Hand.jpeg",
        "assets/images/ryno-crypto/bitcoin-art/ryno-crypto-btc-robot-hand-art-886x886-v1-0.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Bitcoin Art/BTC-Jesus.png",
        "assets/images/ryno-crypto/bitcoin-art/ryno-crypto-btc-jesus-art-1024x1024-v1-0.png",
    ),
    # Banners
    (
        "media/Ryno Crypto Mining Marketing/Banners/TerraHash_Stack-Tech_Stack.png",
        "assets/images/shared/banners/terrahash-stack-tech-stack-banner-1024x1536-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-future_of_mining-300x250-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-future-of-mining-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-liquid_cooled_AI_optimized-300x250-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-liquid-cooled-ai-optimized-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-ryno_crypto_terrahash_stack-300x250-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-terrahash-stack-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-ryno_mining-terrahash_stack-v1.0-cc.jpg",
        "assets/images/shared/banners/ryno-mining-terrahash-stack-banner-1024x1024-v1-0-cc.jpg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-sustainable_btc_mininig-300x250-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-sustainable-btc-mining-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-sustainable_scalable_mining-300x250-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-sustainable-scalable-mining-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/ryno-mining-scalable-solutions-v1.0-cc.png",
        "assets/images/shared/banners/ryno-mining-scalable-solutions-banner-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-mining_evolved-160x600-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-mining-evolved-banner-1024x1536-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/ryno-mining-renewable-energy-v1.0-cc.png",
        "assets/images/shared/banners/ryno-mining-renewable-energy-banner-1024x1536-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/ryno_terrahash_stack_banner-v1.0-cc.jpeg",
        "assets/images/shared/banners/ryno-terrahash-stack-banner-1086x724-v1-0-cc.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-cut_costs-728x90-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-cut-costs-banner-1536x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-cut_costs-v2.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-cut-costs-banner-1536x1024-v2-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/banner-ryno_terrahash_stack-v1.0-cc.png",
        "assets/images/shared/banners/ryno-crypto-ryno-terrahash-stack-banner-1536x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Banners/ryno-terrahash-banner-v1.0-cc.jpg",
        "assets/images/shared/banners/ryno-terrahash-banner-1536x1024-v1-0-cc.jpg",
    ),
    # Logos
    (
        "media/Ryno Crypto Mining Marketing/Logos/bitcoin_mining-v1.0-cc.png",
        "assets/images/shared/logos/bitcoin-mining-logo-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/btc_terrahash_stack-v1.0-cc.png",
        "assets/images/shared/logos/btc-terrahash-stack-logo-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_crypto_mining_services-logo-blue-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-crypto-mining-services-logo-blue-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_crypto-graffiti-color-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-crypto-graffiti-color-logo-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno-logo-street_style-bw-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-logo-street-style-bw-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_crypto-graffiti-bw-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-crypto-graffiti-bw-logo-2048x2048-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_miner_aggressive-graffiti-bw-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-miner-aggressive-graffiti-bw-logo-2048x2048-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_miner_cartoon-graffiti-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-miner-cartoon-graffiti-logo-2048x2048-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_miner_crash-graffiti-bw-v1.0-cc.png",
        "assets/images/ryno-crypto/logos/ryno-miner-crash-graffiti-bw-logo-2048x2048-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/btc_terrahash_stack-512x512-v1.0-cc.png",
        "assets/images/terrahash-stack/logos/btc-terrahash-stack-logo-512x512-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/terrahash_stack-logo-v1.0-cc.jpeg",
        "assets/images/terrahash-stack/logos/terrahash-stack-logo-886x886-v1-0-cc.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_crypto-services-v1.0-cc.jpeg",
        "assets/images/ryno-crypto/logos/ryno-crypto-services-logo-956x1032-v1-0-cc.jpeg",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Logos/ryno_crypto-services-v1.1-cc.png",
        "assets/images/ryno-crypto/logos/ryno-crypto-services-logo-992x1056-v1-1-cc.png",
    ),
    # Infographics
    (
        "media/infographics/terrahash_infographic_1_system_architecture_v2.png",
        "assets/diagrams/infographics/terrahash-infographic-system-architecture-1536x1024-v2-0.png",
    ),
    (
        "media/infographics/terrahash_infographic_2_rebalancing_process_v2.png",
        "assets/diagrams/infographics/terrahash-infographic-rebalancing-process-1024x1536-v2-0.png",
    ),
    (
        "media/infographics/terrahash_infographic_3_dual_strategy_v2.png",
        "assets/diagrams/infographics/terrahash-infographic-dual-strategy-1024x1024-v2-0.png",
    ),
    (
        "media/infographics/terrahash_infographic_4_yield_generation_v2.png",
        "assets/diagrams/infographics/terrahash-infographic-yield-generation-1536x1024-v2-0.png",
    ),
    (
        "media/infographics/terrahash_infographic_5_comparison_matrix_v2.png",
        "assets/diagrams/infographics/terrahash-infographic-comparison-matrix-1536x1024-v2-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Infographics/ryno-mining-market-growth-v1.0-cc.png",
        "assets/diagrams/infographics/ryno-mining-market-growth-1600x1200-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Infographics/terrahash_stack_features-v1.0-cc.png",
        "assets/diagrams/infographics/terrahash-stack-features-2400x1600-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Infographics/ryno-mining-pitch-deck-v1.0.png",
        "assets/diagrams/infographics/ryno-mining-pitch-deck-4770x2670-v1-0.png",
    ),
    # TerraHash Stack Art
    (
        "media/Ryno Crypto Mining Marketing/TerraHash Stack Art/ai_liquid_cooling-v1.0-cc.png",
        "assets/images/terrahash-stack/ai-liquid-cooling-art-1536x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/TerraHash Stack Art/terrahash_mining_facility-v1.0-cc.png",
        "assets/images/terrahash-stack/terrahash-mining-facility-art-1536x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/TerraHash Stack Art/terrahash-lab-v1.0-cc.png",
        "assets/images/terrahash-stack/terrahash-lab-art-1536x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/TerraHash Stack Art/terrahash-liquidcooling-v1.0-cc.png",
        "assets/images/terrahash-stack/terrahash-liquidcooling-art-1024x1024-v1-0-cc.png",
    ),
    # Mining Container Art
    (
        "media/Ryno Crypto Mining Marketing/Mining Container Art/ryno-street_stencil-v1.0-cc.png",
        "assets/images/ryno-crypto/mining-container/ryno-street-stencil-art-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Mining Container Art/ryno-street_art-v1.0-cc.png",
        "assets/images/ryno-crypto/mining-container/ryno-street-art-2048x2048-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Mining Container Art/ryno-street_art-v1.1-cc.png",
        "assets/images/ryno-crypto/mining-container/ryno-street-art-2048x2048-v1-1-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Mining Container Art/ryno-street_art-v1.2-cc.png",
        "assets/images/ryno-crypto/mining-container/ryno-street-art-2048x2048-v1-2-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Mining Container Art/ryno-street_stencil-v1.1-cc.png",
        "assets/images/ryno-crypto/mining-container/ryno-street-stencil-art-2048x2048-v1-1-cc.png",
    ),
    # Wharton Facility
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/container_cutaway_3d_final.png",
        "assets/images/shared/wharton-facility/terrahash-container-cutaway-3d-diagram-1536x1024-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Wharton_Texas-facility_aerial_view.png",
        "assets/images/shared/wharton-facility/wharton-texas-facility-aerial-view-photo-1536x1024-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Wharton_Texas-facility_elevated.png",
        "assets/images/shared/wharton-facility/wharton-texas-facility-elevated-photo-1536x1024-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Wharton_Texas-facility_night.png",
        "assets/images/shared/wharton-facility/wharton-texas-facility-night-photo-1536x1024-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Wharton_Texas-facility_street_view.png",
        "assets/images/shared/wharton-facility/wharton-texas-facility-street-view-photo-1536x1024-v1-0.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Screenshot 2025-10-22 at 11.00.11.png",
        "assets/images/shared/wharton-facility/wharton-facility-screenshot-1-2934x1598-v1-0-20251022.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Screenshot 2025-10-22 at 11.04.05.png",
        "assets/images/shared/wharton-facility/wharton-facility-screenshot-2-3574x1658-v1-0-20251022.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Screenshot 2025-10-22 at 11.01.34.png",
        "assets/images/shared/wharton-facility/wharton-facility-screenshot-3-3574x1674-v1-0-20251022.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Screenshot 2025-10-22 at 11.03.36.png",
        "assets/images/shared/wharton-facility/wharton-facility-screenshot-4-3574x1694-v1-0-20251022.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/Screenshot 2025-10-22 at 11.01.00.png",
        "assets/images/shared/wharton-facility/wharton-facility-screenshot-5-3574x1714-v1-0-20251022.png",
    ),
    # Ryno Crypto Mining Art
    (
        "media/Ryno Crypto Mining Marketing/Ryno Crypto Mining Art/ryno_head-street_style-v1.0-cc.png",
        "assets/images/ryno-crypto/ryno-head-street-style-art-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Ryno Crypto Mining Art/ryno_mining-stencil-bw-v1.0-cc.png",
        "assets/images/ryno-crypto/ryno-mining-stencil-bw-art-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Ryno Crypto Mining Art/ryno-mining-ai-mining-v1.0-cc.png",
        "assets/images/ryno-crypto/ryno-mining-ai-mining-art-1024x1024-v1-0-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Ryno Crypto Mining Art/ryno_head-v1.1-cc.png",
        "assets/images/ryno-crypto/ryno-head-art-857x665-v1-1-cc.png",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Ryno Crypto Mining Art/ryno-head-v1.0-cc.jpg",
        "assets/images/ryno-crypto/ryno-head-art-857x665-v1-0-cc.jpg",
    ),
    # Social media marketing
    (
        "media/social_media-marketing/terrahash_ad_2_smart_dip_buying_v2.png",
        "assets/images/shared/social-media/terrahash-ad-smart-dip-buying-1024x1024-v2-0.png",
    ),
    (
        "media/social_media-marketing/terrahash_ad_3_yield_while_wait_v2.png",
        "assets/images/shared/social-media/terrahash-ad-yield-while-wait-1024x1024-v2-0.png",
    ),
    (
        "media/social_media-marketing/terrahash_ad_4_price_protection_v2.png",
        "assets/images/shared/social-media/terrahash-ad-price-protection-1024x1024-v2-0.png",
    ),
    (
        "media/social_media-marketing/terrahash_ad_5_defi_advantage_v2.png",
        "assets/images/shared/social-media/terrahash-ad-defi-advantage-1024x1024-v2-0.png",
    ),
    # Videos
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/facility_video_shot1.mp4",
        "assets/videos/wharton-facility-tour-shot-1-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/facility_video_shot2.mp4",
        "assets/videos/wharton-facility-tour-shot-2-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/facility_video_shot3.mp4",
        "assets/videos/wharton-facility-tour-shot-3-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/facility_video_shot4.mp4",
        "assets/videos/wharton-facility-tour-shot-4-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/facility_video_shot5.mp4",
        "assets/videos/wharton-facility-tour-shot-5-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/terrahash_facility_walkthrough.mp4",
        "assets/videos/terrahash-facility-walkthrough-original-v1-0.mp4",
    ),
    (
        "media/Ryno Crypto Mining Marketing/Wharton Facility/terrahash_facility_daytime_walkthrough-new.mp4",
        "assets/videos/terrahash-facility-daytime-walkthrough-original-v2-0.mp4",
    ),
]


def main():
    base_dir = Path("/Users/elvis/Documents/Git/RynoCrypto/ryno-assets")

    # Create necessary subdirectories
    subdirs = [
        "assets/images/ryno-crypto/bitcoin-art",
        "assets/images/ryno-crypto/logos",
        "assets/images/ryno-crypto/mining-container",
        "assets/images/terrahash-stack/logos",
        "assets/images/shared/banners",
        "assets/images/shared/logos",
        "assets/images/shared/wharton-facility",
        "assets/images/shared/social-media",
    ]

    for subdir in subdirs:
        (base_dir / subdir).mkdir(parents=True, exist_ok=True)

    # Process file mappings
    copied_count = 0
    skipped_count = 0

    for old_path, new_path in file_mappings:
        old_file = base_dir / old_path
        new_file = base_dir / new_path

        if not old_file.exists():
            print(f"⚠️  Source not found: {old_path}")
            skipped_count += 1
            continue

        # Copy file
        print(f"✓ {old_file.name} → {new_path}")
        shutil.copy2(old_file, new_file)
        copied_count += 1

    print("\n✅ Media reorganization complete!")
    print(f"   Copied: {copied_count} files")
    print(f"   Skipped: {skipped_count} files")


if __name__ == "__main__":
    main()
