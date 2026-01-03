###################  List → Ordered, allows duplicates, mutable ##############################
marks_list = [90, 85, 90, 70]

##What this means
## 1. Order matters ✅
## 2. Duplicates allowed ✅ (90 appears twice)
## 3. You can modify it ✅
marks_list[1] = 88
print(marks_list)   # [90, 88, 90, 70]

## Use when
## 1. You care about order
## 2. You want index-based access


################################# Set → Unordered, unique elements, mutable ##############################
marks_set = {90, 85, 90, 70}

## What this means
## 1. Order does NOT matter ❌
## 2. Duplicates removed automatically ❌
## 3. Fast membership checks ✅

print(marks_set)    # {70, 85, 90}

print(90 in marks_set)  # True (very fast)

##Use when
## 1. You need unique values
## 2. You want to remove duplicates
## 3. You want fast lookups

##################################  Tuple → Ordered, allows duplicates, immutable ##############################
marks_tuple = (90, 85, 90, 70)

##What this means
## Order matters ✅
## Duplicates allowed ✅
## Cannot be changed ❌

marks_tuple[1] = 88   # ❌ TypeError

## Use when
## Data should NOT change (fixed data)
## You want safety & slightly better performance

########################## Dictionary → Key–Value pairs, ordered, fast lookup ##############################
marks_dict = {
    "Math": 90,
    "Science": 85,
    "English": 70
}

## What this means
## Data stored as key → value
## Keys must be unique
## Fast lookup by key

print(marks_dict["Math"])  # 90

## Use when
## You need meaningful access using a key
## JSON / API responses
## Configs, mappings


# ⚡ One Practical Example (Automation mindset)
# users = ["admin", "guest", "admin"]      # list (duplicates)
# unique_users = set(users)                # set
# credentials = ("admin", "password123")   # tuple (fixed)
# user_roles = {"admin": "ALL", "guest": "READ"}  # dict

