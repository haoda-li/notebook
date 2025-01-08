# Protobuf Basics
HLO files and debug_info files are stored in protocol buffer format.
https://developers.google.com/protocol-buffers/docs/pythontutorial


KaenaProto
https://code.amazon.com/packages/KaenaProto/releases

## Message Definition in `.proto`
The definition file for message type, will be compiled for specific programming language. 

```proto
// c style comments 

/** 
 *    preferred for multline comments
 */

// syntax must be the first non-empty, non-comment line of the file
// if not defined, use proto2 as default
syntax = "proto3";

// define a message type
message SearchRequest {
  // each filed type as 
  // {TYPE} {NAME} = {FIELD NUMBER}
  string query = 1;
  int32 page_number = 2;
  int32 results_per_page = 3;
}
```

### Field Number
Each field needs a field number between $1$ and $536,870,911 = 2^{29} - 1$. The range is related to how protobuf encode the message. There are some restrictions: 
- must be unique
- cannot be changed once in use
- should never be reused 
- `19000 - 19999` are reserved. 

The rationale behind is simple: protobuf encode each message field as the field number. If we mutate the field number definition, already existing data will be corrupted. Check [Protobuf encoding](#appendix-encoding) for details. 

### Field Cardinality
For each field, if the field is not set, protobuf will return the default value based on the field type. 

```proto
message SearchRequest {
  
  // For singular type, implicit and optional is almost the same
  // the only difference is that implicit does not preserve field
  // presence when the field is set to default value
  // if we store query = "", queryOpt = "" in the data
  // has_query() will be False, has_queryOpt() will be True

  // implicit 
  string query = 1;
  // optional
  optional string queryOpt = 4;

  // repeated: the field can be repeated zero or more times, with
  // the order being preserved
  repeated int32 page_number = 2;
  // map: self explanatory. Although in implementation is just a 
  // repeated field of key-value pairs.
  // useful to store unstructured data in a proto 
  map map<string, int32> results_per_page = 3;
}
```

### Nested Types

A message field can be another message type. 

```proto
message SearchResponse {
  repeated Result results = 1;
}

message Result {
  string url = 1;
  string title = 2;
  repeated string snippets = 3;
}
```

### Deleting/Modifying a Field

Renaming the field name is generally okay for the default implementation, but highly unrecommended. TextProto or JSON encoding serialize the field name so that renaming a field name will cause issues under these implementations. 

You can delete a field from the definition, but you can never reuse the deleted field number (consider how existing data are encoded). Therefore, when a field is deleted, add the field number (and field name as well for safety) to the `reserved` list in the `.proto` definition. Future developer will get an error if they try to use a reserve entry. 

```proto
message Foo {
  // same as 2, 15, 9, 10, 11
  reserved 2, 15, 9 to 11;
  reserved "foo", "bar";
}
```

### Enumerations
Similar to `enum` in C, and the default value for a enum type is the first element and must be 0. 

```proto
enum Corpus {
  CORPUS_UNSPECIFIED = 0;
  CORPUS_UNIVERSAL = 1;
  CORPUS_WEB = 2;
  CORPUS_IMAGES = 3;
  CORPUS_LOCAL = 4;
  CORPUS_NEWS = 5;
  CORPUS_PRODUCTS = 6;
  CORPUS_VIDEO = 7;
}

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 results_per_page = 3;
  Corpus corpus = 4;
}
```

### Import message definitions
The protocol compiler searches for imported files in a set of directories specified on the protocol compiler command line using the `-I/--proto_path` flag. If no flag was given, it looks in the directory in which the compiler was invoked. In general you should set the `--proto_path` flag to the root of your project and use fully qualified names for all imports.

```proto
import "myproject/other_protos.proto";
```

## C++ API

### Message Class

Each message definition will be compiled into a class with 

```c++
// parser and serializer from/to binary string
bool ParseFromString(const string &data);
bool SerializeToString(string* output) const;

string DebugString();// return a string giving the text_format representation

Foo(); // Default constructor.
~Foo(); // Default destructor.
Foo(const Foo& other); // Copy constructor.
Foo(Foo&& other); // Move constructor.
Foo& operator=(const Foo& other); // Assignment operator.
Foo& operator=(Foo&& other); // Move-assignment operator.
void Swap(Foo* other); // Swap content with another message.
```


### Singular Field
Each scalar fields `foo` will generate the following accessor methods

```c++
// define the field in .proto as 
// int32 foo = 1;
int32 foo() const;
void set_foo(int32 value);
void clear_foo(); // clear the field, and has_foo() will be False 
```

If a field is defined with `optional` (check [Field Cardinality](#field-cardinality) for field presence), then we have the method to check presence

```c++
// define the field in .proto as 
// optional int32 foo = 1;
bool has_foo();
```

Thanks for the c++ string pointer mess, for `string` field we also have

```c++
void set_foo(const string& value);

// for c-style char array, terminated by /0 or but size
void set_foo(const char* value);
void set_foo(const char* value, int size);

string* mutable_foo(); // Returns a pointer to the mutable string object that stores the field’s value. 
```

### Nested Message Field

Note that message as a field is always `optional`. Thus 

```c++
// assume we have a message class Bar, and the field definition
// Bar bar = 1;

bool has_bar() const; 
const Bar& bar() const;
Bar* mutable_bar(); // return a pointer to the mutable Bar object
void clear_bar();
void set_allocated_bar(Bar *bar); // set the object and frees the previous field value
Bar* release_bar(); // release the ownership of the field and returns the pointer to the Bar object
```

### Repeated Fields
Use scalar field as an example, string field is similar but has a few more methods for C-style `char *`
```c++
// define the field in .proto as 
// repeated int32 foo = 1;
int foo_size() const; // return number of elements
const int32 foo(int index) const;  // index is 0-indexed
void set_foo(int index, int32 value);
void add_foo(int32 value); // append to the end
void clear_foo(); // remove all elements
const RepeatedField<int32>& foo() const; // RepeatedField provides STL-lke iterator and other methods
RepeatedField<int32>* mutable_foo(); // Returns a pointer to the underlying mutable RepeatedField
```

### Map field
In general, this is good enough to use a map field. Treat `google::protobuf::Map` as a commonly-used subset of `std::map` or `std::unordered_map`. 
```c++
// define the field in .proto as 
// map<int32, int32> weight = 1;

const google::protobuf::Map<int32, int32>& weight(); // Returns an immutable Map.
google::protobuf::Map<int32, int32>* mutable_weight(); // Returns a mutable Map
```

## Appendix: Data Encoding 
https://protobuf.dev/programming-guides/encoding/#structure