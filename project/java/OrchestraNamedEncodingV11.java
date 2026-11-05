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
  An encoding block that names the encoding standard it is for.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraNamedEncodingV11 extends OrchestraBaseEncodingV11 {

  private String fixrStandard;


}