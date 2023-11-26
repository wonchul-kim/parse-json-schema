from pydantic import BaseModel, Field
from typing import List, Literal

class Test(BaseModel):
    a: float = Field(ge=0, le=1, frozen=True)
    b: float = Field(ge=0, le=1, frozen=True)
    c: float = Field(ge=0, le=1, frozen=True)

class HSV(BaseModel):
    h: float = Field(ge=0, le=1, frozen=True)
    s: float = Field(ge=0, le=1, frozen=True)
    v: float = Field(ge=0, le=1, frozen=True)
    test: Test

class Customs(BaseModel):
    hsv: HSV
    degrees: float = Field(ge=0, le=1, frozen=True)

class ImageCompression(BaseModel):
    p: float = Field(ge=0, le=1, frozen=True)
    quality_lower: float = Field(ge=0, le=100, frozen=True)

class Albumentations(BaseModel):
    Blur: float = Field(ge=0, le=1, frozen=True)
    ImageCompression: ImageCompression

class AugmentationConfig(BaseModel):
    Albumentations: Albumentations
    Customs: Customs

class NetworkConfig(BaseModel):
    backbone: Literal['efficientnetb0', 'efficientnetb1', 'efficientnetb2'] = Field(frozen=True)
    width: int = Field(256, ge=32, frozen=True)
    height: int = Field(256, ge=32, frozen=True)
    channel: int = Field(ge=1, frozen=True)

class TrainConfig(BaseModel):
    device: Literal['gpu', 'cpu'] = Field(frozen=True)
    device_ids: List[int] = Field(frozen=True)
    learning_rate: float = Field(frozen=True)

class Configs(BaseModel):
    train_config: TrainConfig
    augmentation_config: AugmentationConfig
    network_config: NetworkConfig
