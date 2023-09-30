The labeled false alarm cases that exhibit false alarm patterns are listed below:

> For instance, we observed 31 FPs due to the depth of orthogonal slicing being 1, which is already acknowledged in the CryptoGuard paper [1], and thus we do not show the details here.

- The 31 FPs are shown in the `/crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms`: 

  - #1 in `rule3-analysis.md`
  - #9 in `rule3-analysis.md`
  - #62 in `rule3-analysis.md`
  - #4 in `rule9-analysis.md` 



Pattern #1

> We implemented this refinement in CryptoGuard, rerun it on the app data set, and found a large number of FPs for rules 1– 3, 8, 10, 12–13 because of the same root cause, as shown in Table IV.

- The results of our refined CryptoGuard are in the `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/result_def-use-fix_rulebased`. Please note that the rule number in our artifact is accordding to tool implementation. The mapping between the rule number in the paper and the tool is shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/README.md`
- Since the experiment running the total F-droid dataset requires 30h+ time on our server, we provide a scale-down version of the experiment between refined cryptoguard and original cryptoguard. Please refer to the epxeriment E1.



Pattern #2

> In our experiments, we observed 23 FPs due to this string matching bug.

- The 23 FPs are shown in the `/crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms`
  - #6 in `rule3-analysis.md`
  - #47 in `rule3-analysis.md`
  - #138 in `rule3-analysis.md`



Pattern #3

> In our sampled data, we observed 24 HardCodedError FPs in KeyStore, and 28 FPs in PBEKeySpec due to this bug.

- The 24 HardCodedError FPs are shown in the `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`
  - #5, #8 in `KeyStore.md`
  - #1, #2, #3, #5, #6, #8, #9, #10 in `PBEKeySpec.md`



Pattern #4

> Through sampling, we observed that this bug led 1 FP for rule 3, 28 FPs for rule 4, and 113 FPs for rule 6.

- The above FPs are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/verified_misuses/`
  - 1 FP for rule 3: #7 in `Rule-3.md`
  - 28 FPs for rule 4: #1 in `Rule-4.md`
  - 113 FPs for rule 6: #2, #3, #4, #5 in `Rule-6-1.md`



Pattern #5

> In our experiment, we found at least 34 FPs for TypestateError and 80 FPs for IncompleteOperationError due to this.

- The 34 FPs for TypestateError are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`
  - #10 in `MessageDigest.md`
  - #1, #2, #4, #5, #7, #8, #9, #10 in `KeyPairGenerator.md`



Pattern #6

> We found 22 ConstraintError in PBEKeySpec (and 2 in PBEParameterSpec) to be false alarms because of this.

- The 22 ITPs for ConstraintError are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`
  - #2, #6, #11, #21, #32, #42, #45, #50, #51, #56, #57, #59, #60, #66, #68, #69, #72 in `PBEKeySpec.md`
  - #5, #6 in `PBEParameterSpec.md`



Pattern #7

> Overall, we found 53.3% (16/30) of all the rule 15 alarms are ITPs because of this.

- The 16 ITPs of rule 15 alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule5-analysis.md`
  - #2, #4, #5, #8, #10, #11 in  `rule5-analysis.md`.



Pattern #8

> We found 8 additional rule 15 false alarms from CryptoGuard due to exception handling, a representative example of which can be found in the JJWT library5.

- The 8 ITPs of rule 15 alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule5-analysis.md`
  - #1 in `rule5-analysis.md`



Pattern #10

> Nonetheless, the session parameter influences the return value via the if statement. We found 7 false alarms that follow this pattern in our sampling exercise.

- The 7 false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule6-analysis.md`
  - #19, #44, #63, #64, #79, #91 in `rule6-analysis.md`



> In the end, we found 15 false alarms due to (1), but did not observe examples of (2).

- The 15 false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule12-analysis.md`
  - #7, #8 in `rule12-analysis.md`



Pattern #11

> We observed at least 280 false alarms because of this. Likewise, in AES-SIV, a synthetic IV is generated from input instead of SecureRandom. We observed at least 37 false alarms caused by this.

- The 280 false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`
  - #1, #5, #7 in `Cipher.md`
  - #1, #2, #4, #10 in `IvParameterSpec.md`
  - #1, #3, #7 in `PBEKeySpec.md`
  - #2 in `PBEParameterSpec.md`
  - #1, #2 in `SecretKeySpec.md`
- The 37 false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`
  - #8, #9 in `IvParameterSpec.md`



Pattern #12

> We observed 549 false alarms of RequiredPredicateError due to this pattern.

- The 549 false alarms contains above 280 ones due to decryption context and 37 ones due to SIV mode, and other 232 are also shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms`.
  - #3, #4, #5, #6, #7, #8, #9, #10 in `SecretKeySpec.md`
  - #3, #4, #6, #9, #10 in `Cipher.md`
  - #9 in `PBEKeySpec.md`



Pattern #13

> Such omissions caused 96.2% (331/344) of the KeyStore constraint errors reported by CogniCryptSAST to be ITPs.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/KeyStore.md`



> Similarly, the constraints for TrustManagerFactory omitted a common factory name on Android (*i.e.*, X509), thus all 46 of the reported con- straint errors for TrustManagerFactory are ITPs.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/TrustManagerFactory.md`



> Moreover, PKCS7Padding is an alias of PKCS5Padding on Android, but the former is excluded in the whitelist constraints for the Cipher class, thus 20.9% (150/716) of all the ConstraintError for Cipher are ITPs.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/Cipher.md`



> We found that 92.6% (1704/1840) of all the ConstraintError reported for SSLContext are ITPs because of this.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/SSLContext.md`



> This led to 720 ITPs for TrustManagerFactory and 1130 ITPs for SSLContext.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/TrustManagerFactory.md` and `crypto-detectors-evaluation-artifacts/experiment/crysl-exp/verified_alarms/SSLContext.md`



Pattern #15

> For Crypto- Guard’s rule 11, we found 57 alarms concern the use of AES/ECB/NOPADDING. Upon closer inspection, 22 (38%) of them are in fact ITPs.

- The all rule 11 alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/result_nofix_rulebased/rule1` and verifed ones are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule1-analysis.md`



Pattern #16

> CryptoGuard’s rule 9, which detects any usage of java.util.Random, has the highest number of alarms among its 16 rules. Upon closer inspection, we found 2602 cases in the top-10 contributing methods to be ITPs.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule13-analysis.md`



> Through manual sampling, we observed 272 false alarms due to rand being used in non-security-critical contexts, ...

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/verified_misuses/Rule-6-1.md` and `Rule-6-2.md`



Pattern #17

> There are in total 1645 alarms for rule 7, and the 610 alarms from the top-10 contributing methods all appear to be ITPs,

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule7-analysis.md`



Pattern #18

>  Through manual sampling, we found 72 false alarms because of that. 

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule2-analysis.md`



Pattern #19

> Because of this, we observed 30 ITPs for CryptoGuard’s rule 16 contributed by apps that contain DNSSEC libraries such as org.minidns.dnssec and org.xbill.dns.

> Likewise, to implement support for Bitcoin Script [59], wallet apps have to use SHA-1, as it is one of the opcodes. This led to 8 ITPs for CryptoGuard’s rule 16. Moreover, we found that AES/ECB/NOPADDING is also needed for decrypting and validating the permission string in encrypted Adobe PDF (Algorithm 3.13 of [13]). This led to 2 additional ITPs for CryptoGuard’s rule 11.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms`
  - DNSSEC cases are #49, #60 in `rule2-analysis.md`
  - Bitcoin Script cases are #92, #589, #590 in `rule2-analysis.md`
  - PDF cases are #52 in `rule1-analysis.md`



> Overall, this contributes to 56 alarms of CryptoGuard’s rule 2, and 32.5% (233/716) of its rule 11 and 14 alarms

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule1-analysis.md`



> Likewise, for CryptoREX, NTLM also contributed 478 rule 1 alarms, due to its use of DES-ECB.

- The false alarms are shown in `crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/verified_misuses/Rule-1.md`