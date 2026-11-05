package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The encoding blocks of one element, one for each encoding standard that needs more information about it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraEncodingsV11  {

  private List<OrchestraNamedEncodingV11> fixrEncoding;


}