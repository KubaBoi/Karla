# Karla

## Contents

- [/notifications](#1-notifications)
    - [/create](#11-create)
    - [/get](#12-get)
    - [/getAll](#13-getall)
    - [/update](#14-update)
    - [/delete](#15-delete)
    - [/getByRepeat](#16-getbyrepeat)
    - [/getByDescription](#17-getbydescription)
    - [/check](#18-check)
- [/recognition](#2-recognition)
    - [/fromWav](#21-fromwav)
    - [/toMp3](#22-tomp3)
- [/understand](#3-understand)
    - [/text](#31-text)

## RestApi

If there is not an ```Accepts...``` paragraph in endpoint paragraph it means that endpoint does not accepts anything. 

Every endpoint can throw 

### Return Unauthorized - 401

```json
{
    "ERROR": "Unauthorized access"
}
```

It means that user enters wrong credentials while logging in or user does not have right to access endpoint. 

### Return Bad request - 400

```json
{
    "ERROR": "Wrong json structure"
}
```

Request is missing some of necessary parts. And it cannot be done.

<hr>
<hr>

# 1 /notifications

## 1.1 /create

```POST```

Creates new notification

Role = 2

### Accepts post body

```json
{
    "END_TIME": "time with time zone",
    "REPEAT": 0, // time in seconds
    "DESCRIPTION": "str"
}
```

### Return OK - 200

```json
{
    "STATUS": "notification has been created"
}
```

<hr>

## 1.2 /get

```GET```

Get notification by ID

Role = 2

### Accepts path arguments

```json
{
    "id": 0
}
```

### Return OK - 200

```json
{
	"NOTIFICATION": {
		"ID": 0,
		"END_TIME": "time with time zone",
		"REPEAT": 0,
		"DESCRIPTION": "str"
	}
}
```

<hr>

## 1.3 /getAll

```GET```

Get all notifications

### Return OK - 200

```json
{
	"NOTIFICATIONS": [
		{
			"ID": 0,
			"END_TIME": "time with time zone",
			"REPEAT": 0,
			"DESCRIPTION": "str"
		}
	]
}
```

<hr>

## 1.4 /update

```POST```

Updates notfication

Role = 1

### Accepts post body

```json
{
	"ID": 0,
	"END_TIME": "time with time zone",
	"REPEAT": 0,
	"DESCRIPTION": "str"
}
```

### Return OK - 200

```json
{
	"STATUS": "notification has been updated"
}
```

<hr>

## 1.5 /delete

```POST```

Deletes notification

Role = 1

### Accepts post body

```json
{
    "ID": 0
}
```

### Return OK - 200

```json
{
	"STATUS": "notification has been deleted"
}
```

<hr>

## 1.6 /getByRepeat

```GET```

Gets all notifications by REPEAT

Role = 1

### Accepts path arguments

```json
{
    "REPEAT": 0
}
```

### Return OK - 200

```json
{
	"NOTIFICATIONS": [
		{
			"ID": 0,
			"END_TIME": "time with time zone",
			"REPEAT": 0,
			"DESCRIPTION": "str"
		}
	]
}
```

<hr>

## 1.7 /getByDescription

```GET```

Gets all notifications by DESCRIPTION

Role = 1

### Accepts path arguments

```json
{
	"DESCRIPTION": "str"
}
```

### Return OK - 200

```json
{
	"NOTIFICATIONS": [
		{
			"ID": 0,
			"END_TIME": "time with time zone",
			"REPEAT": 0,
			"DESCRIPTION": "str"
		}
	]
}
```

<hr>

## 1.8 /check

```GET```

Return if any notification is done

Role = 1

### Return OK - 200

```json
{
	"NOTIFICATIONS": [
		{
			"DESCRIPTION": "str"
		}
	]
}
```

<hr><hr>

# 2 /recognition

## 2.1 /fromWav

```POST```

Accepts .wav file and return recognized text from it

Role = 1

### Accepts bytes

```Accepts bytes```

### Return OK - 200

```json
{  
	"TEXT": "str"
}
```

### Return No Content - 204

```json
{  
	"TEXT": "I did not understand"
}	
```

<hr>

## 2.2 /toMp3

```POST```

Accepts text and returns .mp3 file from it

Role = 1

### Accepts post body

```json
{  
	"TEXT": "str"
}	
```

### Return OK - 200

```MP3 File```

<hr><hr>

# 3 /understand

## 3.1 /text

```POST```

Accepts ```TEXT``` and ```PINDEX``` and returns logicaly assumed answer. ```PINDEX``` is index of session doing task. For first time it should be -1.

Role = 1

### Accepts post body

```json
{  
	"TEXT": "str",  
	"PINDEX": 0
}	
```

### Return OK - 200

```json
{  
	"TEXT": "str",  
	"DONE": true,  
	"PINDEX": 0
}
```

### Return No Content - 204

```json
{  
	"TEXT": "I did not catch that"
}	
```