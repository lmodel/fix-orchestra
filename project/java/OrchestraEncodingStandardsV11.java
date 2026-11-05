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
  The encoding standards that a repository's encoding blocks name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraEncodingStandardsV11  {

  private List<OrchestraEncodingStandardV11> fixrEncodingStandard;
  private URI xmlBase;


}