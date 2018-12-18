import qualified Data.Counter as C
import qualified Data.Map as M
import qualified Data.Set as S

type HasTwos = Bool
type HasThrees = Bool

hasTwosOrThrees :: String -> (HasTwos, HasThrees)
hasTwosOrThrees line = (keysWithTwos /= [], keysWithThrees /= [])
  where charFreqCounter = C.count line
        keysWithTwos = M.keys $ M.filter (\n -> n == 2) charFreqCounter
        keysWithThrees = M.keys $ M.filter (\n -> n == 3) charFreqCounter

countTrues :: [Bool] -> Int
countTrues bools = foldl (flip ((+) . fromEnum)) 0 bools

linesWithTwosOrThrees :: [(HasTwos, HasThrees)] -> (Int, Int)
linesWithTwosOrThrees counts =
  let twosThrees = unzip counts
      hasTwosList = fst twosThrees
      hasThreesList = snd twosThrees
  in
    (countTrues hasTwosList, countTrues hasThreesList)

checksum :: [String] -> Int
checksum lines = twos * threes
  where (twos, threes) = linesWithTwosOrThrees $ map hasTwosOrThrees lines

diff :: (String, String) -> (Int, String)
diff (s1, s2) = ((max (length s1) (length s2)) - (length lettersInCommon), lettersInCommon)
  where lettersInCommon = [l1 | (l1,l2) <- zip s1 s2, l1 == l2]

findMostSimilar :: [String] -> S.Set String
findMostSimilar lines = S.fromList [letters | (d,letters) <- map diff $ [(l1,l2) | l1 <- lines, l2 <- lines], d == 1]

main :: IO ()
main = do
  f <- readFile("../inputs/02-input")
  putStrLn $ show $ checksum $ lines f
  putStrLn $ show $ findMostSimilar $ lines f
