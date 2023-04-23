package HiddingMsgDNA;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class FrequentWords {
    
    public static void main(String[] args) {
        String text = "AAAAAATGCCACAACACCACCACGCCTGCTGCAATGTGTGTGCTGTGTGCCACTGTGCGCCAAAATGCGCCCACGCCTGCTGAAAAAATGTGCAAAATGGCCTGCTGCCACTGCTGCACGCCTGCTGCGCCTGCACCACTGTGCTGAACACTGGCCTGAACACAATGTGTGCGCCTGCAAAATGCTGCACTGCGCCTGCGCCTGCTGGCCAAGCCAACACCACTGCACTGTGCCACTGC";
        int k = 5;
        int d = 2;
        // List<String> result = frequentWordsWithMismatchesAndReverseComplements(text, k, d);
        // System.out.println(String.join(" ", result));
        List<String> r = generateNeighbors("CGTTACTCT", 2);
        System.out.println(String.join(" ", r));
    }
    
    public static List<String> frequentWordsWithMismatchesAndReverseComplements(String text, int k, int d) {
        Set<String> frequentPatterns = new HashSet<String>();
        Map<String, Integer> patternsMap = new HashMap<String, Integer>();
        for (int i = 0; i <= text.length() - k; i++) {
            String pattern = text.substring(i, i + k);
            List<String> neighbors = generateNeighbors(pattern, d);
            for (String neighbor : neighbors) {
                patternsMap.put(neighbor, patternsMap.getOrDefault(neighbor, 0) + 1);
            }
        }
        for (Map.Entry<String, Integer> entry : patternsMap.entrySet()) {
            String pattern = entry.getKey();
            int count = entry.getValue();
            String rcPattern = reverseComplement(pattern);
            if (!rcPattern.equals(pattern)) {
                count += patternsMap.getOrDefault(rcPattern, 0);
            }
            if (count >= getMaximumCount(patternsMap, d)) {
                frequentPatterns.add(pattern);
            }
        }
        return new ArrayList<String>(frequentPatterns);
    }
    
    public static List<String> generateNeighbors(String pattern, int d) {
        if (d == 0) {
            return Arrays.asList(pattern);
        }
        if (pattern.length() == 1) {
            return Arrays.asList("A", "C", "G", "T");
        }
        List<String> nucleotides = Arrays.asList("A", "C", "G", "T");
        List<String> neighborhood = new ArrayList<String>();
        String suffix = pattern.substring(1);
        List<String> suffixNeighbors = generateNeighbors(suffix, d);
        for (String neighbor : suffixNeighbors) {
            if (hammingDistance(suffix, neighbor) < d) {
                for (String nucleotide : nucleotides) {
                    neighborhood.add(nucleotide + neighbor);
                }
            } else {
                neighborhood.add(pattern.substring(0, 1) + neighbor);
            }
        }
        return neighborhood;
    }
    
    public static int hammingDistance(String p, String q) {
        if (p.length() != q.length()) {
            return -1;
        }
        int distance = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) != q.charAt(i)) {
                distance++;
            }
        }
        return distance;
    }
    
    public static String reverseComplement(String pattern) {
        StringBuilder sb = new StringBuilder();
        for (int i = pattern.length() - 1; i >= 0; i--) {
            char c = pattern.charAt(i);
            switch (c) {
                case 'A':
                    sb.append('T');
                    break;
                case 'C':
                    sb.append('G');
                    break;
                case 'G':
                    sb.append('C');
                    break;
                case 'T':
                    sb.append('A');
                    break;
                default:
                    break;
            }
        }
        return sb.toString();
    }
    
    public static int getMaximumCount(Map<String, Integer> patternsMap, int d) {
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : patternsMap.entrySet()) {
            String pattern = entry.getKey();
            int count = entry.getValue();
            String rcPattern = reverseComplement(pattern);
            if (!rcPattern.equals(pattern)) {
                count += patternsMap.getOrDefault(rcPattern, 0);
            }
            if (count > maxCount) {
                maxCount = count;
            }
        }
        return maxCount;
    }
}



