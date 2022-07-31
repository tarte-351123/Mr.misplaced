from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Any, List
import motor.motor_asyncio
import models
import asyncio
from datetime import datetime, date
# from bson.objectid import ObjectId
from bson import ObjectId


app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:password@localhost:27017/admin?retryWrites=true&w=majority')
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.okiwasure  # .の後ろがコレクション(テーブル)名

@app.post("/date/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.TimeModel = Body(...)):
    """

    ----------
    Parameters:  
    time:  時間  
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["date"].create_index("hostname")
        await db["date"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/user/", response_description="Add new user", tags=["UserController"])
async def create_user(user: models.AddUserModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    user_id: BLEビーコンのmacアドレス  
    name: slack名  
    team: 班名  
        
    """
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    user = jsonable_encoder(user)
    user['is_active'] = True

    try:
        # 既に登録されている名前は登録できないようにする
        await db["user"].create_index("name", unique=True)
        await db["user"].insert_one(user)
    except:
        raise HTTPException(status_code=400, detail=f"Name: '{user['name']}' is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state": f"{user['name']} Add OK!"})

@app.post("/ohashi01_phone/", response_description="Add new user", tags=["UserController"])
async def create_user(user: models.DataModel = Body(...)):

    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    user = jsonable_encoder(user)
    user['is_active'] = True

    try:
        # 既に登録されている名前は登録できないようにする
        await db["ohashi01_phone"].create_index("name", unique=True)
        await db["ohsahi01_phone"].insert_one(user)
    except:
        raise HTTPException(status_code=400, detail=f"Name: '{user['name']}' is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state": f"{user['name']} Add OK!"})

@app.post("/ohashi01_wallet/", response_description="Add new user", tags=["UserController"])
async def create_user(user: models.DataModel = Body(...)):

    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    user = jsonable_encoder(user)
    user['is_active'] = True

    try:
        # 既に登録されている名前は登録できないようにする
        await db["ohashi01_wallet"].create_index("name", unique=True)
        await db["ohsahi01_wallet"].insert_one(user)
    except:
        raise HTTPException(status_code=400, detail=f"Name: '{user['name']}' is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state": f"{user['name']} Add OK!"})

@app.post("/ohashi01_bag/", response_description="Add new user", tags=["UserController"])
async def create_user(user: models.DataModel = Body(...)):

    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    user = jsonable_encoder(user)
    user['is_active'] = True

    try:
        # 既に登録されている名前は登録できないようにする
        await db["ohashi01_bag"].create_index("name", unique=True)
        await db["ohsahi01_bag"].insert_one(user)
    except:
        raise HTTPException(status_code=400, detail=f"Name: '{user['name']}' is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state": f"{user['name']} Add OK!"})

@app.post("/phone/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    user_id: BLEビーコンのmacアドレス  
    name: slack名  
    team: 班名  
        
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["phone"].create_index("hostname")
        await db["phone"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})


@app.post("/result_phone/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddFixDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    count: 経過時間
    time:  時間  
    rssi1: リビングでの電波強度
    rssi2: 玄関での電波強度
    place: 推定場所
    place_num: 
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["result_phone"].create_index("hostname")
        await db["result_phone"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/wallet/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    user_id: BLEビーコンのmacアドレス  
    name: slack名  
    team: 班名  
        
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["wallet"].create_index("hostname")
        await db["wallet"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/result_wallet/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddFixDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    count: 経過時間
    time:  時間  
    rssi1: リビングでの電波強度
    rssi2: 玄関での電波強度
    place: 推定場所
    place_num: 
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["result_wallet"].create_index("hostname")
        await db["result_wallet"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/bag/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    user_id: BLEビーコンのmacアドレス  
    name: slack名  
    team: 班名  
        
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["bag"].create_index("hostname")
        await db["bag"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/result_bag/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddFixDataModel = Body(...)):
    """
    ユーザーの登録

    ----------
    Parameters:  
    count: 経過時間
    time:  時間  
    rssi1: リビングでの電波強度
    rssi2: 玄関での電波強度
    place: 推定場所
    place_num: 
    """
    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["time"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["time"] = (data["time"])

    try:
        await db["result_bag"].create_index("hostname")
        await db["result_bag"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/pattern/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.AddPatternModel = Body(...)):

    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    print(type(data["date"]))
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    data["date"] = (data["date"])

    try:
        await db["pattern"].create_index("hostname")
        await db["pattern"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})

@app.post("/cluster/", response_description="Add new data", tags=["dataController"])
async def create_data(data: models.ClusterModel = Body(...)):

    print("-----")
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    data = jsonable_encoder(data)
    
    # print(datetime.strptime(data["time"],'%Y-%m-%d %H:%M:%S'))
    print(data["normalDistribution"] )

    try:
        await db["cluster"].create_index("hostname")
        await db["cluster"].insert_one(data)
    except:
        raise HTTPException(status_code=400, detail=f"Name: data is already been registered")
    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    # created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state":"OK"})
    
# 統合した
# @app.get("/user/", response_description="List all users", response_model=List[models.ReturnUserModel], tags=["UserController"])
# async def list_users():
#     users = await db["user"].find().to_list(1000)
#     return users


# @app.get("/{id}", response_description="Get a single user", response_model=models.UserModel)
# async def show_user(id: str):
#     if (user := await db["user"].find_one({"_id": id})) is not None:
#         return user

#     raise HTTPException(status_code=404, detail=f"user {id} not found")


# @app.get("/user/{name}", response_description="Get a single user", response_model=models.UserModel)
# async def get_single_user(name: str):
#     if (user := await db["user"].find_one({"name": name})) is not None:
#         return user

#     raise HTTPException(status_code=404, detail=f"name '{name}' not found")

@app.get("/date/", response_description="Get a single data", response_model=List[models.TimeModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """


    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")
        print(await db["date"].count_documents({}))
        if (users := await db["date"].find().to_list(await db["date"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["date"].find({"time": time}).to_list(await db["date"].count_documents({"time": time}))) is not None and time is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["date"].find({"time": time}).to_list(1)) is not None and time is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {time} not found")

@app.get("/user/", response_description="Get a single user", response_model=List[models.UserModel], tags=["UserController"])
async def show_user(user_id: str = None, name: str = None):
    """
    ## ユーザー情報の取得

    ----------
    ### Parameters:  
    **user_id**：BLEビーコンのmacアドレス  
    **name**：slack名   
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータに'user_id'と'name'の両方が含まれていた場合はエラーを返す
    if user_id is not None and name is not None:
        # raise HTTPException(status_code=400, detail="パラメータに'user_id'と'name'の両方が含まれています")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Error": "パラメータに'user_id'と'name'の両方が含まれています"})

    # パラメータが設定されていなかったら全てのデータを返す
    if user_id is None and name is None:
        if (users := await db["user"].find().to_list(1000000)) is not None:
            return users

    # 該当するuserIDのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["user"].find({"user_id": user_id}).to_list(await db["user"].count_documents({"user_id": user_id}))) is not None and user_id is not None:
        return user

    # 該当するnameのユーザ情報を返す
    if (user := await db["user"].find({"name": name}).to_list(1)) is not None and name is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {user_id} not found")


@app.get("/phone/", response_description="Get a single data", response_model=List[models.DataModel], tags=["dataController"])
async def show_data(hostname: str = None, ble_id: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータに'hostname'と'ble_id'の両方が含まれていた場合はエラーを返す
    if hostname is not None and ble_id is not None:
        # raise HTTPException(status_code=400, detail="パラメータに'user_id'と'name'の両方が含まれています")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Error": "パラメータに'user_id'と'name'の両方が含まれています"})

    # パラメータが設定されていなかったら全てのデータを返す
    if hostname is None and ble_id is None:
        print("=====")
        print(await db["phone"].count_documents({}))
        if (users := await db["phone"].find().to_list(await db["phone"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["phone"].find({"hostname": hostname}).to_list(await db["phone"].count_documents({"hostname": hostname}))) is not None and hostname is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["phone"].find({"ble_id": ble_id}).to_list(1)) is not None and ble_id is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {hostname} not found")

@app.get("/result_phone/", response_description="Get a single data", response_model=List[models.FixDataModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")
        print(await db["result_phone"].count_documents({}))
        if (users := await db["result_phone"].find().to_list(await db["result_phone"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["result_phone"].find({"time": time}).to_list(await db["date"].count_documents({"time": time}))) is not None and time is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["result_phone"].find({"time": time}).to_list(1)) is not None and time is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {time} not found")

@app.get("/bag/", response_description="Get a single data", response_model=List[models.DataModel], tags=["dataController"])
async def show_data(hostname: str = None, ble_id: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータに'hostname'と'ble_id'の両方が含まれていた場合はエラーを返す
    if hostname is not None and ble_id is not None:
        # raise HTTPException(status_code=400, detail="パラメータに'user_id'と'name'の両方が含まれています")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Error": "パラメータに'user_id'と'name'の両方が含まれています"})

    # パラメータが設定されていなかったら全てのデータを返す
    if hostname is None and ble_id is None:
        print("=====")
        print(await db["bag"].count_documents({}))
        if (users := await db["bag"].find().to_list(await db["bag"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["bag"].find({"hostname": hostname}).to_list(await db["bag"].count_documents({"hostname": hostname}))) is not None and hostname is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["bag"].find({"ble_id": ble_id}).to_list(1)) is not None and ble_id is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {hostname} not found")

@app.get("/result_bag/", response_description="Get a single data", response_model=List[models.FixDataModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")
        print(await db["result_bag"].count_documents({}))
        if (users := await db["result_bag"].find().to_list(await db["result_bag"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["result_bag"].find({"time": time}).to_list(await db["date"].count_documents({"time": time}))) is not None and time is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["result_bag"].find({"time": time}).to_list(1)) is not None and time is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {time} not found")


@app.get("/wallet/", response_description="Get a single data", response_model=List[models.DataModel], tags=["dataController"])
async def show_data(hostname: str = None, ble_id: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータに'hostname'と'ble_id'の両方が含まれていた場合はエラーを返す
    if hostname is not None and ble_id is not None:
        # raise HTTPException(status_code=400, detail="パラメータに'user_id'と'name'の両方が含まれています")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Error": "パラメータに'user_id'と'name'の両方が含まれています"})

    # パラメータが設定されていなかったら全てのデータを返す
    if hostname is None and ble_id is None:
        print("=====")
        print(await db["wallet"].count_documents({}))
        if (users := await db["wallet"].find().to_list(await db["wallet"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["wallet"].find({"hostname": hostname}).to_list(await db["wallet"].count_documents({"hostname": hostname}))) is not None and hostname is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["wallet"].find({"ble_id": ble_id}).to_list(1)) is not None and ble_id is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {hostname} not found")

@app.get("/result_wallet/", response_description="Get a single data", response_model=List[models.FixDataModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")
        print(await db["result_wallet"].count_documents({}))
        if (users := await db["result_wallet"].find().to_list(await db["result_wallet"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["result_wallet"].find({"time": time}).to_list(await db["date"].count_documents({"time": time}))) is not None and time is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["result_wallet"].find({"time": time}).to_list(1)) is not None and time is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {time} not found")

@app.get("/pattern/", response_description="Get a single data", response_model=List[models.AddPatternModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")
        print(await db["result_wallet"].count_documents({}))
        if (users := await db["pattern"].find().to_list(await db["pattern"].count_documents({}))) is not None:
            return users

    # 該当するhostnameのユーザ情報を返す
    # await db["user"].count_documents({"user_id": user_id})で該当するデータ数を数えている
    if (user := await db["pattern"].find({"time": time}).to_list(await db["date"].count_documents({"time": time}))) is not None and time is not None:
        return user

    # 該当するble_idのユーザ情報を返す
    if (user := await db["pattern"].find({"time": time}).to_list(1)) is not None and time is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {time} not found")

@app.get("/cluster/", response_description="Get a single data", response_model=List[models.ClusterModel], tags=["dataController"])
async def show_data(time: str = None,):
    """
    ----------
    ### Parameters:  
    **hostname**：データを受信した機器の名前
    **rssi**：電波の強さ 
    **ble_id**:データを送信した機器の名前
    **time**:データが送信された時間
    #### (パラメータが設定されてない場合は全データを返します)
    """

    # パラメータが設定されていなかったら全てのデータを返す
    if time is None :
        print("=====")

        if (users := await db["cluster"].find().to_list(await db["cluster"].count_documents({}))) is not None:
            return users


    raise HTTPException(status_code=404, detail=f"user {time} not found")

@app.put("/user/{name}", response_description="Update a user", tags=["UserController"])
async def update_user(name: str, user: models.UpdateUserModel = Body(...)):

    # 受け取ったJSONデータを辞書型に変換
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await db["user"].update_one({"name": name}, {"$set": user})

        # modified_countで更新を実行した際の変更数をカウント
        # 1なら(変更があったら)変更されたデータを返す
        if update_result.modified_count == 1:
            if 'name' not in user:
                # 名前の変更がないときは"name"を使って検索
                if (updated_user := await db["user"].find_one({"name": name})) is not None:
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"state": f"{name}'s Data Change OK!"})
            else:
                # 名前の変更があるときは"user['name']"を使って検索
                if (updated_user := await db["user"].find_one({"name": user["name"]})) is not None:
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"state": f"{user['name']}'s Data Change OK!"})

    # 更新データに変更点が何もなければ元のデータを返す
    if (existing_user := await db["user"].find_one({"name": name})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"state": f"{name}'s Data Not Change"})

    raise HTTPException(status_code=404, detail=f"user {name} not found")


@app.delete("/user/{name}", response_description="Delete a user", tags=["UserController"])
async def delete_user(name: str):
    delete_result = await db["user"].delete_one({"name": name})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200":f"name '{name}' deleate OK!"})

    raise HTTPException(status_code=404, detail=f"user {name} not found")


@app.delete("/phone/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["phone"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/result_phone/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["result_phone"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")


@app.delete("/wallet/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["wallet"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/result_wallet/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["result_wallet"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/bag/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["bag"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/result_bag/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["result_bag"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/cluster/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["cluster"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")

@app.delete("/date/", response_description="Delete a data", tags=["dataController"])
async def delete_data():
    delete_result01 = await db["date"].delete_one({})

    if delete_result01.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200 data deleate OK!"})

    raise HTTPException(status_code=404, detail=f"data not found")


@app.post("/", response_description="Add new Current Infomationn", response_model=models.AfterAddCurrentInfoModel, tags=["CurrentInfoController"])
async def create_current_Info(current_info: models.CurrentInfoModel = Body(...)):
    """
    現在の情報の登録

    ----------
    Parameters:  
    name: slack名   
        
    """
    # Pydanticモデルのようなオブジェクトを受け取り、辞書型にして返す
    current_info = jsonable_encoder(current_info)
    current_info['room'] = ''
    current_info['is_stay'] = False
    current_info['lastTime'] = datetime.now()

    # insert_oneメソッドのレスポンスには、新しく作成された受講者の_idが含まれます。
    try:
        await db["currentInfo"].create_index("name", unique=True)
        new_current_info = await db["currentInfo"].insert_one(current_info)
    except:
        raise HTTPException(status_code=400, detail=f"Name: {current_info['name']} is already been registered")

    # 受講者をコレクションに挿入したら、inserted_idを使用して正しいドキュメントを検索し、これをJSONResponseに返します。
    created_current_info = await db["currentInfo"].find_one({"_id": new_current_info.inserted_id})
    # print(created_current_info)
    # 201コードを返す
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"state": f"{current_info['name']} Add OK!"})


@app.get("/", response_description="List all current info", response_model=List[models.retCurrentInfoModel], tags=["CurrentInfoController"])
async def list_current_infos():
    infos = await db["currentInfo"].find().to_list(1000)
    ret_list = []
    for d in infos:
        # 該当するnameのユーザ情報を取得する
        try:
            user_info = await db["user"].find_one({"name": d['name']})
            # is_active が Falseのものを弾く
            if user_info['is_active']:
                ret_list.append(user_info | d)  # _IDが上書きされてしまうが使わないので無視
        except:
            pass
    return ret_list


@app.get("/{query}", response_description="Get a currentInfo", response_model=List[models.retCurrentInfoModel], tags=["CurrentInfoController"])
async def show_current_info(name: str = None, room: str = None):

    # パラメータに'name'と'room'の両方が含まれていた場合はエラーを返す
    if name is not None and room is not None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Error": "パラメータに'name'と'room'の両方が含まれています"})

    # 名前が指定されていた時の処理
    # 該当するnameのユーザ情報を取得する
    if name is not None:
        user_info = await db["user"].find_one({"name": name})
        if user_info is None:
            raise HTTPException(status_code=404, detail=f"data not found")

        # 該当するnameのユーザ情報を返す
        if (currentInfo := await db["currentInfo"].find({"name": name}).to_list(1)) is not None and user_info['is_active']:
            return [user_info | currentInfo[0]]

    # 部屋名が指定されていた時の処理
    # 該当するroomのユーザ情報を返す
    if (currentInfo := await db["currentInfo"].find({"room": room}).to_list(await db["currentInfo"].count_documents({"room": room}))) is not None and room is not None:
        ret_list = []
        for d in currentInfo:
            # 該当するnameのユーザ情報を取得する
            user_info = await db["user"].find_one({"$and": [{"name": d["name"]}, {"is_active": True}]})
            if user_info is not None:
                ret_list.append(user_info | d)  # _IDが上書きされてしまうが使わないので無視
        return ret_list

    raise HTTPException(status_code=404, detail=f"data not found")


@app.put("/{student-room}", response_description="Update current_info", response_model=List[models.UpdateResultModel], tags=["CurrentInfoController"])
async def update_student_room_current_info(datas: List[models.UpdateCurrentInfoModel] = Body(...)):

    # 受け取ったJSONデータを辞書型に変換
    users = []
    for data in datas:
        users.append({k: v for k, v in data.dict().items() if v is not None})

    # currentInfoに登録されている全ての名前を取得
    registered_names = [user['name'] for user in await db["currentInfo"].find().to_list(1000)]

    # currentInfoに登録されていない名前がusersに入っていたら404を返す
    ret_messages = [{'name': user['name'], 'log': 'データベースに登録されていません'} for user in users if user['name'] not in registered_names]
    if len(ret_messages) > 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ret_messages)

    # 全ユーザ情報を取得
    # 受け取ったデータの中から滞在判定の人の名前情報だけを抜き出す
    get_stay_names = [i['name'] for i in users if i['is_stay'] == True]

    # currentInfo内の送られてきたデータと同じ部屋で滞在判定になっている人の名前情報だけを抜き出す
    # データ数が0の時に部屋名が取れない問題をどうにかする
    current_stay_names = [i['name'] for i in await db["currentInfo"].find({"room": "学生部屋", "is_stay": True}).to_list(1000)]

    # 帰宅した人の名前を抽出する
    no_stay_names = [name for name in current_stay_names if name not in get_stay_names]

    # 滞在判定になっている人の処理
    return_datas = []
    for i in no_stay_names:
        # 滞在判定になっている人の中で，送られてきたデータに入っていない名前の人のroomを""にis_stayをFalseにする
        await db["currentInfo"].update_one({"name": i}, {"$set": {"lastTime": datetime.now(), "room": "", "is_stay": False}})
        return_datas.append({"name": i, "log": "is_stay -> false"})

        # 今日の日付のログデータを検索
        today_log = await db["log"].find_one({'date': date.today().strftime('%Y-%m-%d'), 'name': i})

        # すでに登録されている時間を読み込む
        period = today_log['period']

        # exit_timeに現在の時間を追記
        period[-1]['exit_time'] = datetime.now()
        await db["log"].update_one({'_id': today_log['_id']}, {"$set": {"period": period}})

    # 送られてきたデータを登録する
    for user in users:
        if len(user) >= 1 and user['is_stay']:
            await db["currentInfo"].update_one({"name": user['name']}, {
                "$set": {
                    "lastTime": datetime.now(),
                    "room": user['room'],
                    "is_stay": True
                }
            })
            return_datas.append({"name": user['name'], "log": "is_stay -> true"})

            # ログテーブルへの書き込み
            await db["currentInfo"].update_one({"date": date.today().strftime('%Y-%m-%d')}, {
                "$set": {
                    "lastTime": datetime.now(),
                    "room": "",
                    "is_stay": False
                }
            })

            # 今日の日付のログデータを検索
            today_log = await db["log"].find_one({'date': date.today().strftime('%Y-%m-%d'), 'name': user['name']})

            # 今日のログデータがまだ登録されていなかったら現在の時間を新規登録
            if today_log is None:
                await db["log"].insert_one({
                    "_id": str(ObjectId()),
                    'date': date.today().strftime('%Y-%m-%d'),
                    'name': user['name'],
                    'period': [
                        {
                            'enter_time': datetime.now(),
                            'exit_time': None
                        }]
                })

            # すでにデータが登録されていたら追記する
            elif today_log is not None and today_log['period'][-1]['exit_time'] is not None:
                # すでに登録されている時間を読み込む
                period = today_log['period']
                period.append({'enter_time': datetime.now(), 'exit_time': None})
                await db["log"].update_one({'_id': today_log['_id']}, {"$set": {"period": period}})

        # elif len(user) >= 1 and not user['is_stay']:
        #     return_datas.append({"name": user['name'], "log": "No Change!"})

    if len(return_datas) > 0:
        return return_datas

    raise HTTPException(status_code=404, detail=f"Received malformed data")


@app.put("/{master-room}", response_description="Update current_info", response_model=List[models.UpdateResultModel], tags=["CurrentInfoController"])
async def update_master_room_current_info(
        datas: List[models.UpdateCurrentInfoModel] = Body(...)):

    # 受け取ったJSONデータを辞書型に変換
    users = []
    for data in datas:
        users.append({k: v for k, v in data.dict().items() if v is not None})

    # currentInfoに登録されている全ての名前を取得
    registered_names = [user['name'] for user in await db["currentInfo"].find().to_list(1000)]

    # currentInfoに登録されていない名前がusersに入っていたら404を返す
    ret_messages = [{'name': user['name'], 'log': 'データベースに登録されていません'} for user in users if user['name'] not in registered_names]
    if len(ret_messages) > 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ret_messages)

    # 全ユーザ情報を取得
    # 受け取ったデータの中から滞在判定の人の名前情報だけを抜き出す
    get_stay_names = [i['name'] for i in users if i['is_stay'] == True]

    # currentInfo内の送られてきたデータと同じ部屋で滞在判定になっている人の名前情報だけを抜き出す
    # データ数が0の時に部屋名が取れない問題をどうにかする
    current_stay_names = [i['name'] for i in await db["currentInfo"].find({"room": "院生部屋", "is_stay": True}).to_list(1000)]

    # 帰宅した人の名前を抽出する
    no_stay_names = [name for name in current_stay_names if name not in get_stay_names]

    # 滞在判定になっている人の処理
    return_datas = []
    for i in no_stay_names:
        # 滞在判定になっている人の中で，送られてきたデータに入っていない名前の人のroomを""にis_stayをFalseにする
        await db["currentInfo"].update_one({"name": i}, {"$set": {"lastTime": datetime.now(), "room": "", "is_stay": False}})
        return_datas.append({"name": i, "log": "is_stay -> false"})

        # 今日の日付のログデータを検索
        today_log = await db["log"].find_one({'date': date.today().strftime('%Y-%m-%d'), 'name': i})

        # すでに登録されている時間を読み込む
        period = today_log['period']

        # exit_timeに現在の時間を追記
        period[-1]['exit_time'] = datetime.now()
        await db["log"].update_one({'_id': today_log['_id']}, {"$set": {"period": period}})

    # 送られてきたデータを登録する
    for user in users:
        if len(user) >= 1 and user['is_stay']:
            await db["currentInfo"].update_one({"name": user['name']}, {
                "$set": {
                    "lastTime": datetime.now(),
                    "room": user['room'],
                    "is_stay": True
                }
            })
            return_datas.append({"name": user['name'], "log": "is_stay -> true"})

            # ログテーブルへの書き込み
            await db["currentInfo"].update_one({"date": date.today().strftime('%Y-%m-%d')}, {
                "$set": {
                    "lastTime": datetime.now(),
                    "room": "",
                    "is_stay": False
                }
            })

            # 今日の日付のログデータを検索
            today_log = await db["log"].find_one({'date': date.today().strftime('%Y-%m-%d'), 'name': user['name']})

            # 今日のログデータがまだ登録されていなかったら現在の時間を新規登録
            if today_log is None:
                await db["log"].insert_one({
                    "_id": str(ObjectId()),
                    'date': date.today().strftime('%Y-%m-%d'),
                    'name': user['name'],
                    'period': [
                        {
                            'enter_time': datetime.now(),
                            'exit_time': None
                        }]
                })

            # すでにデータが登録されていたら追記する
            elif today_log is not None and today_log['period'][-1]['exit_time'] is not None:
                # すでに登録されている時間を読み込む
                period = today_log['period']
                period.append({'enter_time': datetime.now(), 'exit_time': None})
                await db["log"].update_one({'_id': today_log['_id']}, {"$set": {"period": period}})

        # elif len(user) >= 1 and not user['is_stay']:
        #     return_datas.append({"name": user['name'], "log": "No Change!"})

    if len(return_datas) > 0:
        return return_datas

    raise HTTPException(status_code=404, detail=f"Received malformed data")


@app.delete("/{name}", response_description="Delete current_info", tags=["CurrentInfoController"])
async def delete_current_info(name: str):
    delete_result = await db["currentInfo"].delete_one({"name": name})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"200":f"name '{name}' delete OK!"})

    raise HTTPException(status_code=404, detail=f"user {name} not found")


# 時間を指定してフィルタをかける例
# @app.get("/time/{time}", response_description="Get a time user", response_model=List[models.dataModel], tags=["DataController"])
# async def get_time_user(time: int):
#     start = datetime.now() - timedelta(seconds=time)
#     end = datetime.now()
#     if (user := await db["data"].find({"timestamp": {'$lt': end, '$gte': start}}).to_list(1000)) is not None:
#         return user
#     raise HTTPException(status_code=404, detail=f"name '{time}' not found")