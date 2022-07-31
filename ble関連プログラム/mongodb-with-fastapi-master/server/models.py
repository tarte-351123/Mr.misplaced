from re import I
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, time, timedelta
from typing import Optional, List
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    user_id: str = Field(...)
    name: str = Field(max_length=30)
    team: str = Field(...)
    is_active: bool = Field(...)
    # gpa: float = Field(..., le=4.0)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_id": "MAC Address",
                "name": "ogane",
                "team": "ロケーション",
                "is_active": True
            }
        }


class DataModel(BaseModel):
    # 登録の型を決める場合はここを操作
    hostname: str = Field(...)
    rssi: int = Field(...)
    ble_id: str = Field(...)
    time: str = Field(...)
    # gpa: float = Field(..., le=4.0)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "hostname": "ラズパイ1",
                "ble_id": "my_beacon",
            }
        }

class FixDataModel(BaseModel):
    # 登録の型を決める場合はここを操作
    count: int = Field(...) 
    time: str = Field(...)    
    rssi1: int = Field(...) 
    rssi2: int = Field(...) 
    place: str = Field(...) 
    place_num: int = Field(...) 
    # gpa: float = Field(..., le=4.0)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "count": 0 ,
                "time": "2001-01-14 22:22:22",    
                "rssi1": -12,
                "rssi2": -23,
                "place": "リビング",
                "place_num": 2,
            }
        }

class TimeModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    # 登録の型を決める場合はここを操作
    time: str = Field(...)
    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "time": "2001-01-14 22:22:22",
            }
        }

class AddUserModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str = Field(...)
    name: str = Field(max_length=30)
    team: str = Field(...)
    # is_active: bool = Field(...)
    # gpa: float = Field(..., le=4.0)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_id": "MAC Address",
                "name": "ogane",
                "team": "ロケーション"
            }
        }


class AddDataModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    # 登録の型を決める場合はここを操作
    hostname: str = Field(...)
    rssi: int = Field(...)
    ble_id: str = Field(...)
    time: str = Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "hostname": "ラズパイ1",
                "rssi": 60,
                "ble_id": "my_beacon",
                "time": "2021-12-10 16:13:20"
            }
        }
        
class DataModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    # 登録の型を決める場合はここを操作
    hostname: str = Field(...)
    count: int = Field(...)
    time: str = Field(...)
    rssi: int = Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "hostname": "ohashi01",
                "count": 256,
                "time": "2022-07-30 18:18:51",
                "rssi": 60
            }
        }

class AddFixDataModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    # 登録の型を決める場合はここを操作
    count: int = Field(...)
    time: str = Field(...) 
    rssi1: int = Field(...)
    rssi2: int = Field(...)
    place: str = Field(...) 
    place_num: int = Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "count": 0 ,
                "time": "2022-05-19 14:30:15",    
                "rssi1": 34,
                "rssi2": 88,
                "place": "リビング",
                "place_num": 2 
            }
        }


class AddPatternModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    # 登録の型を決める場合はここを操作
    start_time: str = Field(...)
    end_time: str = Field(...)
    date: str = Field(...)
    time: str = Field(...)
    object: str=Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "start_time": "2022-02-22 22:22:22",
                "end_time": "2022-02-23 00:00:00",
                "date": "日曜日",
                "time": "22:20",
                "object": "phone,wallet",
            }
        }
        
class ClusterModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    # 登録の型を決める場合はここを操作
    dateType: str = Field(...)
    normalDistribution: dict = Field(...)
    # mean: str = Field(...)
    # std: str = Field(...)
    # range: list=Field(...)
    # from_: str = Field(...)
    # to_: str = Field(...)
    model: list = Field(...)
    # object: str = Field(...)
    # percentage: str  = Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {  
            "example":{
                "dateType": "date",
                "normalDistribution": {
                    "mean": "11:11",
                    "std": "32",
                    "range": [{
                    "from_": "2021-05-29T22:12:21.804569",
                    "to_": "2021-05-29T22:12:21.804569"
                    },
                    {
                    "from": "2021-05-29T22:12:21.804569",
                    "to": "2021-05-29T22:12:21.804569"
                    }, 
                    {
                    "from": "2021-05-29T22:12:21.804569",
                    "to": "2021-05-29T22:12:21.804569"
                    }, ]
                },
                "model": [{
                    "object": "abc",
                    "percentage": "80"
                    },
                    {
                    "object": "abc",
                    "percentage": "80"  
                    },
                    {
                    "object": "abc",
                    "percentage": "80"
                    }, ]
            }
        }

# class AfterAddUserModel(BaseModel):
#     name: str = Field(...)
#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "state": "ogane Add OK!",
#             }
#         }


# class AfterPutUserModel(BaseModel):
#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "state": "ogane's Data Change OK!",
#             }
#         }

class UpdateUserModel(BaseModel):
    user_id: Optional[str]
    name: Optional[str]
    team: Optional[str]
    is_active: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_id": "MAC Address",
                "name": "slack名",
                "team": "ロケーション",
                "is_active": True
            }
        }


class ReturnUserModel(BaseModel):
    user_id: str = Field(...)
    name: str = Field(...)
    team: str = Field(...)
    is_active: bool = Field(...)

    # email: EmailStr = Field(...)
    # course: str = Field(...)
    # gpa: float = Field(..., le=4.0)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_id": "MAC Address",
                "name": "ogane",
                "team": "ロケーション",
                "is_active": False
            }
        }


class CurrentInfoModel(BaseModel):
    # 変数名に_をつけるとプライベート変数と解釈されてしまうため，alias="_id"で名前を変えている
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    # lastTime: Optional[datetime] = Field(...)
    name: str = Field(...)
    # room: str = Field(...)
    # is_stay: bool = Field(...)

    class Config:
        allow_population_by_field_name = True  # エイリアスを使用するための設定
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "ogane"
            }
        }


class AfterAddCurrentInfoModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "state": "ogane Add OK!",
            }
        }


class UpdateCurrentInfoModel(BaseModel):
    name: Optional[str]
    room: Optional[str]
    is_stay: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "slack名",
                "room": "部屋名(学生部屋 | 院生部屋)",
                "is_stay": True
            }
        }


class UpdateResultModel(BaseModel):
    name: str = Field(...)
    log: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "ogane",
                "log": "is_stay -> true | false"
            }
        }


class retCurrentInfoModel(BaseModel):
    user_id: str = Field(...)
    name: str = Field(...)
    team: str = Field(...)
    is_active: bool = Field(...)
    lastTime: datetime = Field(...)
    room: str = Field(...)
    is_stay: bool = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "user_id": "MAC Address",
            "name": "ogane",
            "team": "ロケーション",
            "is_active": True,
            "lastTime": "2021-05-29T22:12:21.804569",
            "room": "学生部屋",
            "is_stay": True
        }


