commit_message_generator_role = """
You are a helpful coding AI assistant. 
The only task for you is to generate the commit message from git diff file and user input.
"""

commit_message_generator_guidelines = """
I will generate a commit message from the git diff content based on the following guidelines:

```
# Generate Git Commit Message from Git Diff Content

## Generated Commit Message Guidelines

- Keep the commit message concise and descriptive.
- Summarize the changes made in the commit.
- Use imperative mood in commit messages (e.g., "Fix typo" instead of "Fixed typo").
- Include relevant context if necessary.
```
"""

commit_message_generator_format = """
## Example Input

```
diff --git a/.gitignore b/.gitignore
index adf0c38..704518b 100644
--- a/.gitignore
+++ b/.gitignore
@@ -1,3 +1,5 @@
 .idea/
 .venv/
 .idea
+git.log
+
```

## Example Output

```
Update `.gitignore` to exclude `git.log` and remove tracking for `.idea` and `.venv/` directories.
```
"""

commit_message_generator_demo_input = """
    diff --git a/templates/index.html b/templates/index.html
index b05c9d6..14915aa 100644
--- a/templates/index.html
+++ b/templates/index.html
@@ -688,8 +688,8 @@
                         <div class="col-12">
                             <input type="text" class="form-control blastReadChoosingMode" id="blastReadChoosingMode"
                                    name="blastReadChoosingMode"
-                                   value="1"
-                                   placeholder="1">
+                                   required="required" value="{{blastReadChoosingMode}}"
+                                   placeholder="{{blastReadChoosingMode}}">
                         </div>
                     </div>
                 </div>
@@ -1283,8 +1283,8 @@
                         <div class="col-12">
                             <input type="text" class="form-control advanceMode blastParsingMode" id="blastParsingMode"
                                    name="blastParsingMode"
-                                   required="required" value="2"
-                                   placeholder="2">
+                                   required="required" value="{{rbcl_blast_parsing_mode}}"
+                                   placeholder="{{rbcl_blast_parsing_mode}}}">
                         </div>
                     </div>
                 </div>
diff --git a/yml_parser.py b/yml_parser.py
index 6152e23..c18bed6 100644
--- a/yml_parser.py
+++ b/yml_parser.py
@@ -62,9 +62,9 @@ def parsing_yml_to_shell(batch_name: str):
         script += f"minimumOverlapBasePair+=('{str(config['minimum_overlap_base_pair'][i]).strip()}')\n"  # minimumOverlapBasePair
         script += f"maximumMismatchBasePair+=('{str(config['maximum_mismatch_base_pair'][i]).strip()}')\n"  # maximumMismatch
         # Dev Only
-        script += f"blastReadChoosingMode[{i}]='{config['blastReadChoosingMode'][i] if config['blastReadChoosingMode'][i] == '0' else '1'}'\n"
+        script += f"blastReadChoosingMode+=('{str(config['blastReadChoosingMode'][i]).strip()}')\n"
         # blastReadChoosingMode (default: 1): 0: 10Ncat Blast, 1: split R1 R2 Blast
    """

commit_message_generator_demo_output = """
Refactor form inputs in index.html and yml_parser.py

- Updated form inputs in index.html to use dynamic values for 'value' and 'placeholder' attributes.
- Modified yml_parser.py to append values to 'blastReadChoosingMode' and 'blastParsingMode' lists instead of assigning them directly.
"""

commit_message_generator_test_input = """
diff --git a/main/mergeModule/nnSpliter.py b/main/mergeModule/nnSpliter.py
index a090c2e..cadacb0 100644
--- a/main/mergeModule/nnSpliter.py
+++ b/main/mergeModule/nnSpliter.py
@@ -114,4 +114,24 @@ print("[INFO] " + str(process_file_number), " files are split.")
 
 print("[INFO] nnSpliter.py is ended on loci: " + sys.argv[2])
 
-
+# --------------------------------prototype--------------------------------
+# # sample data
+# target="AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCTNNNNNNNNNNAGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
+# r1="AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCT"
+# r2="AGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
+# filename="Teratophyllum_koordersii_Liu9823_KTHU2241_01_1.000_abundance_121_10Ncat"
+# "C:/Users/kwz50/KTHU2241_Liu9823_Teratophyllum_koordersii_.fas"
+
+
+# def nn_spliter(target,r1,r2,filename):
+#     pattern_for_split = r'NNNNNNNNNN'
+#     result=re.split(pattern_for_split,target,maxsplit=1)
+#     if (len(result[0])==len(r1) or len(result[0])==len(r2)) and (len(result[1])==len(r1) or len(result[1])==len(r2)):
+#         return result
+#     else:
+#         print("Incorrect Ns split in ",filename)
+
+# print(nn_spliter(target,r1,r2,filename))
+
+# result1="AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCT"
+# result2="AGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
diff --git a/main/poc/splitter.py b/main/poc/splitter.py
deleted file mode 100644
index bbf61d1..0000000
--- a/main/poc/splitter.py
+++ /dev/null
@@ -1,25 +0,0 @@
-import re
-
-
-# -------------------------------- nnSplitter.py prototype - -------------------------------
-def nn_spliter(target_seq, r1_seq, r2_seq, seq_filename):
-    pattern_for_split = r'NNNNNNNNNN'
-    result = re.split(pattern_for_split, target_seq, maxsplit=1)
-    if (len(result[0]) == len(r1_seq) or len(result[0]) == len(r2_seq)) and (
-            len(result[1]) == len(r1_seq) or len(result[1]) == len(r2_seq)):
-        return result
-    else:
-        print("Incorrect Ns split in ", seq_filename)
-
-
-# sample data
-target = "AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCTNNNNNNNNNNAGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
-r1 = "AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCT"
-r2 = "AGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
-filename = "Teratophyllum_koordersii_Liu9823_KTHU2241_01_1.000_abundance_121_10Ncat"
-"C:/Users/kwz50/KTHU2241_Liu9823_Teratophyllum_koordersii_.fas"
-
-print(nn_spliter(target, r1, r2, filename))
-
-result1 = "AAGCTGGTGTCAAAGATTACCGACTGACCTACTACACCCCCGAATACAAGACCAAAGATACCGATATCTTAGCAGCCTTCCGAATGACCCCACAACCCGGAGTACCAGCTGAAGAAGCCGGAGCTGCGGTAGCTGCAGAATCCTCTACGGGTACGTGGACCACTGTATGGACAGATGGATTGACCAATCTTGACCGTTACAAGGGCCGATGCTACGACATTGAACCCGTCGCTGGGGAAGAGAACCAGTATATCGCGTATGTAGCT"
-result2 = "AGCTTATCCTTTGGATCTATTCGAAGAAGGTTCTGTCACCAATTTGTTCACCTCCATTGTAGGTAATGTCTTCGGATTTAAGGCTCTACGCGCCTTACGCTTGGAAGACCTTCGAATCCCTCCTGCTTATTCTAAAACTTTTATCGGACCGCCTCATGGTATTCAGGTCGAAAGGGATAAACTGAACAAATATGGACGTCCTTTATTGGGATGTACAATCAAGCCAAAATTAGGTCTGTCTGCTAAGAATTATGGTAGAGCCGTCTAT"
"""
