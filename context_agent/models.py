from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ABTestRecord:
    """Data model for A/B test records from CSV"""
    date: str
    device: str
    volume: int
    ab_test: str
    segment: int
    page: Optional[str] = None

    def to_dict(self):
        return {
            "date": self.date,
            "device": self.device,
            "volume": self.volume,
            "ab_test": self.ab_test,
            "segment": self.segment,
            "page": self.page
        }

    def __repr__(self):
        return f"ABTestRecord(date={{self.date}}, device={{self.device}}, volume={{self.volume}}, ab_test={{self.ab_test}}, segment={{self.segment}}, page={{self.page}})"


@dataclass
class SegmentDimensions:
    """Dimensions structure for segments"""
    segment_1: list  # Contains: date, ab_test
    segment_2: list  # Contains: device, volume, page
    
    def __repr__(self):
        return f"SegmentDimensions(segment_1={{self.segment_1}}, segment_2={{self.segment_2}})"