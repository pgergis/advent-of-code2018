import System.Environment
import Data.List.Split
import qualified Data.Counter as C
import qualified Data.Map.Strict as M

type Coord = (Int, Int)
type CoordCounter = C.Counter Coord Int
type Start = Coord
type Height = Int
type Width = Int
type ElfID = String

parseClaim :: String -> (Start, Width, Height, ElfID)
parseClaim claim = ((topLeft !! 0, topLeft !! 1), lxw !! 0, lxw !! 1, startingString !! 0)
  where startingString = splitOn " " claim
        topLeft = map read $ splitOn "," $ init $ startingString !! 2
        lxw = map read $ splitOn "x" $ startingString !! 3

getElfClaim :: String -> (ElfID, [Coord])
getElfClaim claim = (elfID, [(x,y) | x <- xRange, y <- yRange])
  where
    (start, width, height, elfID) = parseClaim claim
    xRange = [(fst start)..(fst start + width - 1)]
    yRange = [(snd start)..(snd start + height - 1)]

getOverlapCounter :: [String] -> CoordCounter
getOverlapCounter inputLines = foldr (\key prev -> C.update key prev) C.empty coordList
  where coordList = concatMap (\elf -> snd $ getElfClaim elf) inputLines

processInput1 :: CoordCounter -> Int
processInput1 counter = foldr overlapCounter 0 counter
  where overlapCounter = \count totalOverlaps -> if count >= 2 then totalOverlaps + 1 else totalOverlaps

processInput2 :: CoordCounter -> [String] -> [ElfID]
processInput2 counter lines = map fst $ filter predicate processed
  where processed = map getElfClaim lines
        predicate = \item -> all (\coord -> (M.lookup coord counter) == Just 1) (snd item)

main = do
  f <- readFile "inputs/03-input"
  putStrLn $ show $ processInput1 $ getOverlapCounter (lines f)
  putStrLn $ show $ processInput2 (getOverlapCounter (lines f)) (lines f)
