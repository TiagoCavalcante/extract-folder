def unique_names(names):
  # Dictionary to ensure each name is unique
  unique = {}

  # Process each name only once
  for name in names:
    unique[name] = True

  # Return the list of unique names sorted
  # alphabetically
  return sorted(unique.keys())


# Input from user, names separated by newline
print(
  "Enter names, separated by pressing Enter"
  " after each name (press Ctrl+D or Ctrl+Z then"
  " Enter to finish):"
)
input_names = []
while True:
  try:
    line = input()
  except EOFError:
    break
  input_names.append(line.strip())

# Get unique names sorted alphabetically
unique = unique_names(input_names)
print("\nUnique names in alphabetical order:")
for name in unique:
  # print(name.upper())
  print(name.upper())
