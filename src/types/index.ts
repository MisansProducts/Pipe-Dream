export interface CityReading {
  city: string;
  timestamp: string | null;
  features: [string, number | null, number | null] | null;
  timezone?: string;
}
