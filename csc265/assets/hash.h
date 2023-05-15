#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define BUCKET_SIZE 10

typedef struct bucket_t {
  unsigned int size;
  unsigned int max_size;
  int *arr;
};

typedef struct hash_table_t {
  int size; // should be a prime number
  bucket_t* buckets;
};

static bool is_prime(int n) {
  assert(n > 0);
  for (int i = 2; i <= sqrt(n); i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}

// Get the smallest prime number that is not less than n (for hash table size
// computation)
int next_prime(int n) {
  for (int i = n;; i++) {
    if (is_prime(i))
      return i;
  }
  assert(false);
  return 0;
}

// Create a hash table with 'size' buckets; the storage is allocated dynamically
// using malloc(); returns NULL on error
hash_table_t *hash_create(int size) {
  assert(size > 0);

  int tsize = next_prime(size);
  hash_table_t *table = (hash_table_t *) malloc(sizeof(hash_table_t));
  if (table == NULL) {
    return NULL;
  }
  table->size = tsize;
	table->buckets = (bucket_t *) malloc(tsize * sizeof(bucket_t));
  if (table->buckets == NULL) {
    free(table);
    return NULL;
  }
  for (int i = 0; i < tsize; i++) {
    int *arr = (int *) malloc(BUCKET_SIZE * sizeof(int));
    (table->buckets[i]).max_size = BUCKET_SIZE;
    (table->buckets[i]).size = 0;
    (table->buckets[i]).arr = arr;
  }
  return table;
}

// Release all memory used by the hash table, its buckets and entries
void hash_destroy(hash_table_t *table) {
  assert(table != NULL);

  for (int i = 0; i < table->size; i++) {
    free((table->buckets[i]).arr);
  }
	free(table->buckets);
	free(table);
}

// Returns 0 if key is not found, 1 if exist
int hash_get(hash_table_t *table, int key) {
  assert(table != NULL);

	int hash_value = key % table->size;
	bucket_t *bucket = &(table->buckets[hash_value]);
  for (int i = 0; i < bucket->size; i++) {
    if (bucket->arr[i] == key) return 1;
  }

  return 0;
}

// Returns 0 on success, -1 on failure
int hash_put(hash_table_t *table, int key) {
  assert(table != NULL);

  int hash_value = key % table->size;
	bucket_t *bucket = &(table->buckets[hash_value]);

  // if already exist, dont need to put
  for (int i = 0; i < bucket->size; i++) {
    if ((bucket->arr)[i] == key) return 0;
  }

  if (bucket->size == bucket->max_size) {
    bucket->max_size *= 2;
    bucket->arr = (int *) realloc(bucket->arr, (bucket->max_size) * sizeof(int));
  }
  bucket->arr[bucket->size++] = key;
  return 0;
}