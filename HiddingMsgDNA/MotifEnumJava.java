package HiddingMsgDNA;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class MotifEnumJava {

    public static Set<String> findMotifs(List<String> dna, int k, int d) {
        Set<String> patterns = new HashSet<String>();
        for (String pattern : generateKmers(k)) {
            boolean found = true;
            for (String sequence : dna) {
                if (!containsWithMismatches(sequence, pattern, d)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                patterns.add(pattern);
            }
        }
        return patterns;
    }

    public static Set<String> generateKmers(int k) {
        Set<String> kmers = new HashSet<String>();
        generateKmers("", k, kmers);
        return kmers;
    }

    private static void generateKmers(String prefix, int k, Set<String> kmers) {
        if (k == 0) {
            kmers.add(prefix);
        } else {
            generateKmers(prefix + "A", k - 1, kmers);
            generateKmers(prefix + "C", k - 1, kmers);
            generateKmers(prefix + "G", k - 1, kmers);
            generateKmers(prefix + "T", k - 1, kmers);
        }
    }

    public static boolean containsWithMismatches(String s, String pattern, int d) {
        for (int i = 0; i <= s.length() - pattern.length(); i++) {
            String substring = s.substring(i, i + pattern.length());
            if (hammingDistance(substring, pattern) <= d) {
                return true;
            }
        }
        return false;
    }

    public static int hammingDistance(String s1, String s2) {
        int count = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        List<String> dna = Arrays.asList("ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT");
        int k = 3;
        int d = 1;
        Set<String> motifs = findMotifs(dna, k, d);
        System.out.println(motifs);
        String h="hola";
        String f=h.substring(0,0+2);
        System.out.println(f);
    }
}
